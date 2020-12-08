import aqi_converter
import pandas as pd
import os
from typing import Dict, List
from matplotlib import pyplot as plt
from matplotlib import dates
import datetime
from dateutil.relativedelta import relativedelta


def parse_file(filepath: str, N_rolling_average=7) -> pd.DataFrame:

    # Read csv file to dataframe.
    df = pd.read_csv(filepath_or_buffer=filepath, delimiter=',')
    data_cols = list(df.columns)[1:]

    # Convert date to datetime datatype
    df['date'] = pd.to_datetime(df['date'])

    # Convert data columns to numerics
    df[data_cols] = df[data_cols].apply(pd.to_numeric, errors='coerce')

    if len(data_cols) > 2:
        # Drop entries without pm measurements
        df = df.drop(df[df[[' pm25', ' pm10']].count(axis=1) == 0].index)
    else:
        df = df.drop(df[df[[' pm25']].count(axis=1) == 0].index)

    # Calculate aqi
    df['AQI'] = df[data_cols].max(axis=1)

    df['Nday_rolling_AQI'] = df['AQI'].rolling(N_rolling_average).mean()

    # Map aqi to bucket values
    df['pollution_level'] = df['AQI'].apply(lambda x: aqi_converter.get_pollution_level(x))

    # Get filename from last entry in filepath and remove .csv extension
    fname = filepath.split('/')[-1][:-4]

    return (fname, df)

def get_dataset_filepaths(parent_dir='waqi_datasets/', subdirs=['asia', 'us', 'eu']) -> Dict[str, List[str]]:
    """Reads filepaths from subdirs in parent dir and returns dict with {subdir: [files_in_subdir]}."""

    return {sdir: list(*os.walk(parent_dir + sdir))[2] for sdir in subdirs}


def get_comparative_dataframe(filepath: str, N_rolling_average=7) -> pd.DataFrame:
    fname, df = parse_file(filepath, N_rolling_average)

    # Pivot table to group table columns by year
    pv = pd.pivot_table(df, index=df['date'].dt.dayofyear, columns=df['date'].dt.year, values='Nday_rolling_AQI')

    # Extract relevant years
    df1 = pv[[2019, 2020]].copy()

    # Convert from ordinal(1-365) dates to regular date values
    df1.index = df1.index.map(datetime.date.fromordinal).map(lambda x: x + relativedelta(years=2019))

    df1.columns = [fname + '-' + str(colname) for colname in df1.columns]

    return df1

def parse_all_datasets(parent_dir='waqi_datasets/', N_rolling_average=7):

    datasets = get_dataset_filepaths()
    r = {}

    for continent, cities in datasets.items():
        r[continent] = [get_comparative_dataframe(parent_dir + continent + '/' + city, N_rolling_average) for city in cities]

    return r


def combined_region_dfs(N_rolling_average=7):
    dfmap = parse_all_datasets(N_rolling_average=N_rolling_average)

    regionlist = {}

    for region, dflist in dfmap.items():
        combined_df = pd.concat(dflist, axis=1, sort=False)

        cols2019 = [colname for colname in combined_df if '2019' in colname]
        cols2020 = [colname for colname in combined_df if '2020' in colname]

        combined_df[region + '-mean-2019'] = combined_df[cols2019].mean(axis=1)
        combined_df[region + '-mean-2020'] = combined_df[cols2020].mean(axis=1)

        regionlist[region] = combined_df

    return regionlist

def plot_regions(path='', plot=True, save=False, N_rolling_average=7):
    dfs = combined_region_dfs(N_rolling_average)

    def get_label(region, year): return region + '-' + str(N_rolling_average) + '-day-rolling-avg-' + str(year)

    for region, df in dfs.items():
        fig = plt.figure()
        ax = plt.gca()

        lines = [region + '-mean-2019', region + '-mean-2020']
        labels = [get_label(region, 2019), get_label(region, 2020)]
        df.plot(kind='line', y=lines, ax=ax, label=labels)

        ax.xaxis.set_major_locator(dates.MonthLocator(interval=1))
        fig.set_figheight(5)
        fig.set_figwidth(15)
        if save:
            plt.savefig(path+region+'_'+str(N_rolling_average)+'day_rolling_average'+'.png')
        if plot:
            plt.show()


if __name__ == "__main__":
    plot_regions(path='../figures/',plot=False, save=True, N_rolling_average=7)
    plot_regions(path='../figures/',plot=False, save=True, N_rolling_average=30)

