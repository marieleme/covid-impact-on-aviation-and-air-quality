from pandas.core.frame import DataFrame
import aqi_converter
import pandas as pd
import os
from typing import Dict, List
from matplotlib import pyplot as plt
from matplotlib import dates
import datetime
import numpy as np
from dateutil.relativedelta import relativedelta

config = {'rolling_avg': 7, 'scale': False}

def set_config(avg, scale):
    config['rolling_avg'] = avg
    config['scale'] = scale

def parse_file(filepath: str) -> pd.DataFrame:

    # Read csv file to dataframe.
    df = pd.read_csv(filepath_or_buffer=filepath, delimiter=',')
    data_cols = list(df.columns)[1:]

    # Convert date to datetime datatype
    df['date'] = pd.to_datetime(df['date'])

    # Convert data columns to numerics
    df[data_cols] = df[data_cols].apply(pd.to_numeric, errors='coerce')

    if ' pm10' in df.columns:
        # Drop entries without pm measurements
        df = df.drop(df[df[[' pm25', ' pm10']].count(axis=1) == 0].index)
    else:
        # Special case for when only pm25 is present
        df = df.drop(df[df[[' pm25']].count(axis=1) == 0].index)

    # Calculate aqi
    df['AQI'] = df[data_cols].max(axis=1)

    # Calculate rolling windows median
    df['Nday_rolling_AQI'] = df['AQI'].rolling(window=config['rolling_avg'], min_periods=1).median()

    # Map aqi to bucket values
    df['pollution_level'] = df['AQI'].apply(lambda x: aqi_converter.get_pollution_level(x))

    # Get filename from last entry in filepath and remove .csv extension
    fname = filepath.split('/')[-1][:-4]

    return (fname, df)

def get_dataset_filepaths(parent_dir='waqi_datasets/', subdirs=['asia', 'us', 'eu']) -> Dict[str, List[str]]:
    """ Reads filepaths from subdirs in parent dir and returns dict with {subdir: [files_in_subdir]}."""

    return {sdir: list(*os.walk(parent_dir + sdir))[2] for sdir in subdirs}


def get_comparative_dataframe(filepath: str) -> pd.DataFrame:
    """reads dataframe from file and pivots data to be columns with a years data"""

    fname, df = parse_file(filepath)

    # Pivot table to group table columns by year
    pv = pd.pivot_table(df, index=df['date'].dt.dayofyear, columns=df['date'].dt.year, values='Nday_rolling_AQI')

    # Extract relevant years
    df1 = pv[[2019, 2020]].copy()

    # Scale values after maximal value
    if config['scale']:
        dfmax = df1[2019].max()
        df1[2019] = df1[2019].apply(lambda x: x/dfmax)
        dfmax = df1[2020].max()
        df1[2020] = df1[2020].apply(lambda x: x/dfmax)

    # Convert from ordinal(1-365) dates to regular date values
    df1.index = df1.index.map(datetime.date.fromordinal).map(lambda x: x + relativedelta(years=2019))

    # Rename all column to include cityname in label 
    df1.columns = [fname + '-' + str(colname) for colname in df1.columns]

    return df1


def parse_all_datasets(parent_dir='waqi_datasets/'):

    datasets = get_dataset_filepaths()
    r = {}

    # Reads all files and maps the comparative dataframes to their region
    for continent, cities in datasets.items():
        r[continent] = [get_comparative_dataframe(parent_dir + continent + '/' + city) for city in cities]

    return r


def combined_region_dfs() -> Dict[str, DataFrame]:
    """ For all regions will return dataframe with 2019 and 2020 data for all cities in region and combined mean
        Returns dict{'us|eu|asia': dataframe}
    """

    dfmap = parse_all_datasets()

    region_dict = {}

    for region, dflist in dfmap.items():
        combined_df = pd.concat(dflist, axis=1, sort=False)

        # Gets list of columns with data for 2019 and 2020
        cols2019 = [colname for colname in combined_df if '2019' in colname]
        cols2020 = [colname for colname in combined_df if '2020' in colname]

        # Calculates mean of 2019 and 2020 related columns into separate columns
        combined_df[region + '-mean-2019'] = combined_df[cols2019].mean(axis=1)
        combined_df[region + '-mean-2020'] = combined_df[cols2020].mean(axis=1)

        # insert finished dataframe into return object
        region_dict[region] = combined_df

    return region_dict


def combine_all_regions(path='', plot=True, save=True, N_rolling_average=7, scale=False):
    set_config(N_rolling_average, scale)
    dfs = combined_region_dfs()

    global_df = pd.concat(dfs.values(), axis=1, sort=False)

    # Get get data from all values 
    cols2019 = [colname for colname in global_df if '2019' in colname and 'mean' not in colname]
    cols2020 = [colname for colname in global_df if '2020' in colname and 'mean' not in colname]

    # Calculates mean of 2019 and 2020 related columns into separate columns
    global_df['global-mean-2019'] = global_df[cols2019].mean(axis=1)
    global_df['global-mean-2020'] = global_df[cols2020].mean(axis=1)

    fig = plt.figure()
    ax = plt.gca()

    global_df.plot(kind='line', y=['global-mean-2019', 'global-mean-2020'], ax=ax)

    ax.xaxis.set_major_locator(dates.MonthLocator(interval=1))

    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    ax.set_xticks(ax.get_xticks().tolist()[:-1])
    ax.set_xticklabels(months)

    fig.set_figheight(5)
    fig.set_figwidth(15)

    fig.tight_layout(pad=3.0)

    plt.xlabel('Start of Month')
    if scale:
            plt.ylabel('Scaled Air quality (AQI)')
            plt.title('Scaled Average global air quality for 2019 and 2020')
    else:
        plt.ylabel('Air quality (AQI)')
        plt.title('Average global air quality for 2019 and 2020')

    if save:
        if scale:
            plt.savefig(path + 'scaled_global_average_rolling7.png')
        else:
            plt.savefig(path + 'global_average_rolling7.png')

    if plot:
        plt.show()


def plot_regions(path='', plot=True, save=False, N_rolling_average=7, scale=False):
    set_config(N_rolling_average, scale)
    dfs = combined_region_dfs()

    def get_label(region, year): 
        if scale:
            return region + '-' + str(N_rolling_average) + '-day-rolling-median-' + str(year)
        else:
            return region + '-' + str(N_rolling_average) + '-day-rolling-median-scaled' + str(year)

    for region, df in dfs.items():
        fig = plt.figure()
        ax = plt.gca()

        lines = [region + '-mean-2019', region + '-mean-2020']
        labels = [get_label(region, 2019), get_label(region, 2020)]
        df.plot(kind='line', y=lines, ax=ax, label=labels)

        ax.xaxis.set_major_locator(dates.MonthLocator(interval=1))

        months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        ax.set_xticks(ax.get_xticks().tolist()[:-1])
        ax.set_xticklabels(months)

        plt.xlabel('Start of Month')
        if scale:
            plt.ylabel('Scaled Air quality (AQI)')
            plt.title('Scaled Average air quality in ' + region + ' for 2019 and 2020')
        else:
            plt.ylabel('Air quality (AQI)')
            plt.title('Average air quality in ' + region + ' for 2019 and 2020')

        fig.set_figheight(5)
        fig.set_figwidth(15)
        fig.tight_layout(pad=3.0)
        if save:
            if scale:
                plt.savefig(path+region+'_scaled_'+str(N_rolling_average)+'day_rolling_average'+'.png')
            else:
                plt.savefig(path+region+'_'+str(N_rolling_average)+'day_rolling_average'+'.png')

        if plot:
            plt.show()


if __name__ == "__main__":
    combine_all_regions(path='../figures/', plot=False, save=True, N_rolling_average=7)
    plot_regions(path='../figures/', plot=False, save=True, N_rolling_average=7)
    plot_regions(path='../figures/', plot=False, save=True, N_rolling_average=30)

    combine_all_regions(path='../figures/', plot=False, save=True, N_rolling_average=7, scale=True)
    plot_regions(path='../figures/', plot=False, save=True, N_rolling_average=7, scale=True)
    plot_regions(path='../figures/', plot=False, save=True, N_rolling_average=30, scale=True)
