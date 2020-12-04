import aqi_converter
import pandas as pd
import os
from typing import Dict, List
from matplotlib import pyplot as plt
import datetime
from dateutil.relativedelta import relativedelta


def parse_file(filepath: str) -> pd.DataFrame:

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

    df['7day_rolling_AQI'] = df['AQI'].rolling(7).mean()

    # Map aqi to bucket values
    df['pollution_level'] = df['AQI'].apply(lambda x: aqi_converter.get_pollution_level(x))

    # Get filename from last entry in filepath and remove .csv extension
    fname = filepath.split('/')[-1][:-4]

    return (fname, df)

def get_dataset_filepaths(parent_dir='waqi_datasets/', subdirs=['asia', 'us', 'eu']) -> Dict[str, List[str]]:
    """Reads filepaths from subdirs in parent dir and returns dict with {subdir: [files_in_subdir]}."""

    return {sdir: list(*os.walk(parent_dir + sdir))[2] for sdir in subdirs}


def get_comparative_dataframe(filepath: str) -> pd.DataFrame:
    fname, df = parse_file(filepath)

    # Pivot table to group table columns by year
    pv = pd.pivot_table(df, index=df['date'].dt.dayofyear, columns=df['date'].dt.year, values='7day_rolling_AQI')

    # Extract relevant years
    df1 = pv[[2019, 2020]].copy()

    # Convert from ordinal(1-365) dates to regular date values
    df1.index = df1.index.map(datetime.date.fromordinal).map(lambda x: x + relativedelta(years=2019))

    df1.columns = [fname + '-' + str(colname) for colname in df1.columns]

    return df1

def parse_all_datasets(parent_dir='waqi_datasets/'):

    datasets = get_dataset_filepaths()
    r = {}

    for continent, cities in datasets.items():
        r[continent] = [get_comparative_dataframe(parent_dir + continent + '/' + city) for city in cities]

    return r

def plot_comparative_df(df, i):
    ax = plt.gca()
    df.plot(kind='line', y=2019, ax=ax)
    df.plot(kind='line', y=2020, ax=ax)
    plt.show()

def combine_region_dfs():
    dfmap = parse_all_datasets()

    regionlist = {}

    for region, dflist in dfmap.items():
        combined_df = pd.concat(dflist, axis=1, sort=False)

        cols2019 = [colname for colname in combined_df if '2019' in colname]
        cols2020 = [colname for colname in combined_df if '2020' in colname]

        combined_df[region + '-mean-2019'] = combined_df[cols2019].mean(axis=1)
        combined_df[region + '-mean-2020'] = combined_df[cols2020].mean(axis=1)

        regionlist[region] = combined_df
        
    print(regionlist)
    return regionlist

def plot_regions():
    dfs = combine_region_dfs()

    for region, df in dfs.items():
        lines = [region + '-mean-2019', region + '-mean-2019']
        df.plot(kind='line', y=lines)


if __name__ == "__main__":
    # print(parse_all_datasets())

    # get_comparative_dataframe('waqi_datasets/us/los-angeles-north main street-air-quality.csv')
    # i = 0
    # for key, value in parse_all_datasets().items():
    #     for fname, df in value:
    #         plot_comparative_df(df, i)
    #         i += 1
    combine_region_dfs()
