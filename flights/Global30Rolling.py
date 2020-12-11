import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

LFPG_df = pd.read_csv("flights/dailyDataSets/LFPG_2019")
EGLL_df = pd.read_csv("flights/dailyDataSets/EGLL_2019")
EHAM_df = pd.read_csv("flights/dailyDataSets/EHAM_2019")
KJFK_df = pd.read_csv("flights/dailyDataSets/KJFK_2019")
KORD_df = pd.read_csv("flights/dailyDataSets/KORD_2019")
KLAX_df = pd.read_csv("flights/dailyDataSets/KLAX_2019")
VIDP_df = pd.read_csv("flights/dailyDataSets/VIDP_2019")
RJTT_df = pd.read_csv("flights/dailyDataSets/RJTT_2019")
VHHH_df = pd.read_csv("flights/dailyDataSets/VHHH_2019")

LFPG_df_2020 = pd.read_csv("flights/dailyDataSets/LFPG_2020")
EGLL_df_2020 = pd.read_csv("flights/dailyDataSets/EGLL_2020")
EHAM_df_2020 = pd.read_csv("flights/dailyDataSets/EHAM_2020")
KJFK_df_2020 = pd.read_csv("flights/dailyDataSets/KJFK_2020")
KORD_df_2020 = pd.read_csv("flights/dailyDataSets/KORD_2020")
KLAX_df_2020 = pd.read_csv("flights/dailyDataSets/KLAX_2020")
VIDP_df_2020 = pd.read_csv("flights/dailyDataSets/VIDP_2020")
RJTT_df_2020 = pd.read_csv("flights/dailyDataSets/RJTT_2020")
VHHH_df_2020 = pd.read_csv("flights/dailyDataSets/VHHH_2020")


def sum_dataframes(airpots, year, airport_names):
    total = 0
    for index, df in enumerate(airpots):
        total += df["30day_rolling_"+ airport_names[index] + " " + year]

    total_df = pd.DataFrame(columns = ['total'])
    total_df['total'] = total

    return total_df


def plot_global_total(df_2019, df_2020):

    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.plot(df_2019['total'], label="2019")
    plt.plot(df_2020['total'], label="2020")

    plt.xticks([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334], months )
    plt.xlim(0,365)

    plt.ylabel('# airplanes')
    plt.xlabel('Month')
    plt.title("All airports 30 days rolling")
    plt.legend()
    plt.savefig("global30days")

def prepare_df(continent='global'):
    airportNames = ["LFPG", "EGLL", "EHAM", "KJFK", "KORD", "KLAX", "VIDP", "RJTT", "VHHH"]
    airports_df_2019 = [LFPG_df, EGLL_df, EHAM_df,KJFK_df,KORD_df, KLAX_df, VIDP_df, RJTT_df,VHHH_df]
    airports_df_2020 = [LFPG_df_2020, EGLL_df_2020, EHAM_df_2020, KJFK_df_2020 ,KORD_df_2020, KLAX_df_2020, VIDP_df_2020, RJTT_df_2020,VHHH_df_2020]

    if continent == 'eu':
        airportNames = ["LFPG", "EGLL", "EHAM"]
        airports_df_2019 = [LFPG_df, EGLL_df, EHAM_df]
        airports_df_2020 = [LFPG_df_2020, EGLL_df_2020, EHAM_df_2020]
    if continent == 'us':
        airportNames = ["KJFK", "KORD", "KLAX"]
        airports_df_2019 = [KJFK_df, KORD_df, KLAX_df]
        airports_df_2020 = [KJFK_df_2020 ,KORD_df_2020, KLAX_df_2020]
    if continent == 'asia':
        airportNames = ["VIDP", "RJTT", "VHHH"]
        airports_df_2019 = [VIDP_df, RJTT_df,VHHH_df]
        airports_df_2020 = [VIDP_df_2020, RJTT_df_2020,VHHH_df_2020]
    
    return airports_df_2019, airports_df_2020, airportNames

def sum_df(continent):
    airports_df_2019, airports_df_2020, airportNames = prepare_df(continent)
    global_df_2019 = sum_dataframes(airports_df_2019, "2019", airportNames)
    global_df_2020 = sum_dataframes(airports_df_2020, "2020", airportNames)

    return global_df_2019, global_df_2020

def plot(continent):
    global_df_2019, global_df_2020 = sum_df(continent)
    plot_global_total(global_df_2019, global_df_2020)

def main():
    plot('global')

if __name__ == "__main__":
    main()