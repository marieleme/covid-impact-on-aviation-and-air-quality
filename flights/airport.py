import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np 

LFPG_df = pd.read_csv("simpleData/LFPG_2019")
EGLL_df = pd.read_csv("simpleData/EGLL_2019")
EHAM_df = pd.read_csv("simpleData/EHAM_2019")
KJFK_df = pd.read_csv("simpleData/KJFK_2019")
KORD_df = pd.read_csv("simpleData/KORD_2019")
KLAX_df = pd.read_csv("simpleData/KLAX_2019")
VIDP_df = pd.read_csv("simpleData/VIDP_2019")
RJTT_df = pd.read_csv("simpleData/RJTT_2019")
VHHH_df = pd.read_csv("simpleData/VHHH_2019")

LFPG_df_2020 = pd.read_csv("simpleData/LFPG_2020")
EGLL_df_2020 = pd.read_csv("simpleData/EGLL_2020")
EHAM_df_2020 = pd.read_csv("simpleData/EHAM_2020")
KJFK_df_2020 = pd.read_csv("simpleData/KJFK_2020")
KORD_df_2020 = pd.read_csv("simpleData/KORD_2020")
KLAX_df_2020 = pd.read_csv("simpleData/KLAX_2020")
VIDP_df_2020 = pd.read_csv("simpleData/VIDP_2020")
RJTT_df_2020 = pd.read_csv("simpleData/RJTT_2020")
VHHH_df_2020 = pd.read_csv("simpleData/VHHH_2020")

airports_europe_2019 = [LFPG_df, EGLL_df, EHAM_df]
airports_usa_2019 = [KJFK_df, KORD_df, KLAX_df]
airports_asia_2019 = [VIDP_df, RJTT_df, VHHH_df]

airports_europe_2020 = [LFPG_df_2020, EGLL_df_2020, EHAM_df_2020]
airports_usa_2020 = [KJFK_df_2020, KORD_df_2020, KLAX_df_2020]
airports_asia_2020 = [VIDP_df_2020, RJTT_df_2020, VHHH_df_2020]

airportNames_europe = ["LFPG", "EGLL", "EHAM"]
airportNames_usa = ["KJFK", "KORD", "KLAX"]
airportNames_asia = ["VIDP", "RJTT", "VHHH"]

def plotsub(airpors_region, airportnames, region, ylim, x):

    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.subplot(2, 1, x)
    for index, df in enumerate(airpors_region):
        plt.plot(df.index.values , df['total'], label =airportnames[index])

    plt.xticks( np.arange(len(months)), months )
    plt.ylabel('# airplanes')
    plt.xlabel('Month')
    plt.title(region)

    axes = plt.gca()
    bottom, top = axes.get_ylim()

    if(ylim != 0):
        plt.ylim(500, ylim + 5000)
    else:
        plt.ylim(500, top + 5000)

    
    plt.legend()

    return top

def main():
    plt.rcParams["figure.figsize"] = [10,6]
    fig, plots = plt.subplots(2,1)
    
    ylim = plotsub(airports_usa_2019, airportNames_usa, "New York, Chicago and LA 2019", 0, 1)
    plotsub(airports_usa_2020, airportNames_usa, "New York, Chicago and LA 2020", ylim, 2)
    fig.tight_layout(pad=3.0)
    plt.savefig("USASub")
    plt.close()


    fig, plots = plt.subplots(2,1)
    ylim = plotsub(airports_asia_2019, airportNames_asia, "Delhi, Tokyo and Hong Kong 2019", 0, 1)
    plotsub(airports_asia_2020, airportNames_asia, "Delhi, Tokyo and Hong Kong 2020", ylim, 2)
    fig.tight_layout(pad=3.0)
    plt.savefig("AsiaSub")
    plt.close()

    fig, plots = plt.subplots(2,1)
    ylim = plotsub(airports_europe_2019, airportNames_europe, "Paris, England and Amsterdam 2019", 0, 1)
    plotsub(airports_europe_2020, airportNames_europe, "Paris, England and Amsterdam 2020", ylim, 2)
    fig.tight_layout(pad=3.0)
    plt.savefig("EuropaSub")
    plt.close()


if __name__ == "__main__":
    main()