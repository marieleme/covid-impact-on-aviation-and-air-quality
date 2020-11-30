import aqi_converter 
import pandas as pd
import os
from typing import Dict, List
from matplotlib import pyplot as plt
import datetime
from dateutil.relativedelta import relativedelta


def parse_file(filename : str) -> pd.DataFrame:

    # Read csv file to dataframe.
    df = pd.read_csv(filepath_or_buffer=filename, delimiter=',')
    data_cols = list(df.columns)[1:]

    # Convert date to datetime datatype
    df['date'] = pd.to_datetime(df['date'])

    # Convert data columns to numerics
    df[data_cols] = df[data_cols].apply(pd.to_numeric, errors='coerce')

    if len(data_cols)>2:
        # Drop entries without pm measurements
        df = df.drop(df[df[[' pm25', ' pm10']].count(axis=1) == 0].index)
    else:
        df = df.drop(df[df[[' pm25']].count(axis=1) == 0].index)


    # Calculate aqi
    df['AQI'] = df[data_cols].max(axis=1)

    df['7day_rolling_AQI'] = df['AQI'].rolling(1).mean()

    # Map aqi to bucket values
    df['pollution_level'] = df['AQI'].apply( lambda x: aqi_converter.get_pollution_level(x))

    return df

def get_dataset_filenames(parent_dir='waqi_datasets/') -> Dict[str, List[str]]:
    """Reads filenames from subdirs in parent dir and returns dict with {subdir: [files_in_subdir]}."""
    subdirs = ['asia', 'us', 'eu']

    return {sdir: list(*os.walk(parent_dir + sdir))[2] for sdir in subdirs}

def get_comparative_dataframe(filename: str) -> pd.DataFrame:
    df = parse_file(filename)

    # Pivot table so yearly values are in same row
    pv = pd.pivot_table(df, index=df['date'].dt.month, columns=df['date'].dt.year, values='7day_rolling_AQI')

    # Extract relevant years
    df1 = pv[[2019, 2020]].copy()

    # Convert from ordinal(1-365) dates to regular date values
    # df1.index = df1.index.map(datetime.date.fromordinal).map(lambda x: x + relativedelta(years=2019))

    return df1

def parse_all_datasets(parent_dir='waqi_datasets/'):

    filepath = lambda cont, city : parent_dir + cont + '/' + city
    datasets = get_dataset_filenames()
    r = {}

    for continent, cities in datasets.items():
        r[continent] = [get_comparative_dataframe(filepath(continent, city)) for city in cities]

    return r

def plot_comparative_df(df, i):
    ax = plt.gca()
    df.plot(kind='line', y=2019, ax=ax)
    df.plot(kind='line', y=2020, ax=ax)
    plt.savefig(f'us{i}.png')
    plt.show()


if __name__ == "__main__":
    # print(parse_all_datasets())

    # get_comparative_dataframe('waqi_datasets/us/los-angeles-north main street-air-quality.csv')
    i = 0
    for key, value in parse_all_datasets().items():
        for df in value:
            plot_comparative_df(df, i)
            i += 1
