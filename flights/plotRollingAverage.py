import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np 
from matplotlib import dates

LFPG_df = pd.read_csv("dailyDataSets/LFPG_2019")
EGLL_df = pd.read_csv("dailyDataSets/EGLL_2019")
EHAM_df = pd.read_csv("dailyDataSets/EHAM_2019")
KJFK_df = pd.read_csv("dailyDataSets/KJFK_2019")
KORD_df = pd.read_csv("dailyDataSets/KORD_2019")
KLAX_df = pd.read_csv("dailyDataSets/KLAX_2019")
VIDP_df = pd.read_csv("dailyDataSets/VIDP_2019")
RJTT_df = pd.read_csv("dailyDataSets/RJTT_2019")
VHHH_df = pd.read_csv("dailyDataSets/VHHH_2019")

LFPG_df_2020 = pd.read_csv("dailyDataSets/LFPG_2020")
EGLL_df_2020 = pd.read_csv("dailyDataSets/EGLL_2020")
EHAM_df_2020 = pd.read_csv("dailyDataSets/EHAM_2020")
KJFK_df_2020 = pd.read_csv("dailyDataSets/KJFK_2020")
KORD_df_2020 = pd.read_csv("dailyDataSets/KORD_2020")
KLAX_df_2020 = pd.read_csv("dailyDataSets/KLAX_2020")
VIDP_df_2020 = pd.read_csv("dailyDataSets/VIDP_2020")
RJTT_df_2020 = pd.read_csv("dailyDataSets/RJTT_2020")
VHHH_df_2020 = pd.read_csv("dailyDataSets/VHHH_2020")

airports_europe_2019 = [LFPG_df, EGLL_df, EHAM_df]
airports_usa_2019 = [KJFK_df, KORD_df, KLAX_df]
airports_asia_2019 = [VIDP_df, RJTT_df, VHHH_df]

airports_europe_2020 = [LFPG_df_2020, EGLL_df_2020, EHAM_df_2020]
airports_usa_2020 = [KJFK_df_2020, KORD_df_2020, KLAX_df_2020]
airports_asia_2020 = [VIDP_df_2020, RJTT_df_2020, VHHH_df_2020]

airportNames_europe = ["LFPG", "EGLL", "EHAM"]
airportNames_usa = ["KJFK", "KORD", "KLAX"]
airportNames_asia = ["VIDP", "RJTT", "VHHH"]

def plotrollingAvg(airpors_region, airportnames, region, year, rollig):

    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for index, df in enumerate(airpors_region):
        values = df[rollig + airportnames[index] + " " +  year].to_numpy()
        plt.plot(values , label =airportnames[index])

    plt.xticks([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334], months )
    plt.xlim(0,365)

    plt.ylabel('# airplanes')
    plt.xlabel('Month')
    plt.title(region + " " + year)
    plt.legend()

def makeSubplot(airpors_2019, airports_2020, airportnames, region, rolling, figName):
    plt.rcParams["figure.figsize"] = [10,5]
    fig, plots = plt.subplots(2,1)

    plt.subplot(2, 1, 1)
    plotrollingAvg(airpors_2019, airportnames, region, "2019", rolling)
    
    plt.subplot(2, 1, 2)
    plotrollingAvg(airports_2020, airportnames,  region, "2020", rolling)

    fig.tight_layout(pad=3.0)
    plt.savefig(figName)
    plt.close()


def main():
    makeSubplot(airports_europe_2019, airports_europe_2020, airportNames_europe, "Paris, England and Amsterdam", '30day_rolling_', "30DaysRollingAvgEurope")
    makeSubplot(airports_usa_2019, airports_usa_2020, airportNames_usa, "New York, Chicago and LA", '30day_rolling_', "30DaysRollingAvgUSA")
    makeSubplot(airports_asia_2019, airports_asia_2020, airportNames_asia, "Delhi, Tokyo and Hong Kong", '30day_rolling_', "30DaysRollingAvgAsia")

if __name__ == "__main__":
    main()