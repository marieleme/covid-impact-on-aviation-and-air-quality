import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np 

LFPG_df = pd.read_csv("flights/simpleData/LFPG_2019")
EGLL_df = pd.read_csv("flights/simpleData/EGLL_2019")
EHAM_df = pd.read_csv("flights/simpleData/EHAM_2019")
KATL_df = pd.read_csv("flights/simpleData/KATL_2019")
KORD_df = pd.read_csv("flights/simpleData/KORD_2019")
KLAX_df = pd.read_csv("flights/simpleData/KLAX_2019")
OMAA_df = pd.read_csv("flights/simpleData/OMAA_2019")
RJTT_df = pd.read_csv("flights/simpleData/RJTT_2019")
VHHH_df = pd.read_csv("flights/simpleData/VHHH_2019")

LFPG_df_2020 = pd.read_csv("flights/simpleData/LFPG_2020")
EGLL_df_2020 = pd.read_csv("flights/simpleData/EGLL_2020")
EHAM_df_2020 = pd.read_csv("flights/simpleData/EHAM_2020")
KATL_df_2020 = pd.read_csv("flights/simpleData/KATL_2020")
KORD_df_2020 = pd.read_csv("flights/simpleData/KORD_2020")
KLAX_df_2020 = pd.read_csv("flights/simpleData/KLAX_2020")
OMAA_df_2020 = pd.read_csv("flights/simpleData/OMAA_2020")
RJTT_df_2020 = pd.read_csv("flights/simpleData/RJTT_2020")
VHHH_df_2020 = pd.read_csv("flights/simpleData/VHHH_2020")

airports_europe_2019 = [LFPG_df, EGLL_df, EHAM_df]
airports_usa_2019 = [KATL_df, KORD_df, KLAX_df]
airports_asia_2019 = [OMAA_df, RJTT_df, VHHH_df]

airports_europe_2020 = [LFPG_df_2020, EGLL_df_2020, EHAM_df_2020]
airports_usa_2020 = [KATL_df_2020, KORD_df_2020, KLAX_df_2020]
airports_asia_2020 = [OMAA_df_2020, RJTT_df_2020, VHHH_df_2020]

airportNames_europe = ["LFPG", "EGLL", "EHAM"]
airportNames_usa = ["KATL", "KORD", "KLAX"]
airportNames_asia = ["OMAA", "RJTT", "VHHH"]

def to_df_helper(df, old_df, nm):
    df[nm] = old_df['Average']
    return df 

def make_list_helper():
    eu_2019 = calculate_moving_average(airports_europe_2019, 12)
    eu_2020 = calculate_moving_average(airports_europe_2020, 10)
    
    us_2019 = calculate_moving_average(airports_usa_2019, 12)
    us_2020 = calculate_moving_average(airports_usa_2020, 10)
    
    asia_2019 = calculate_moving_average(airports_asia_2019, 12)
    asia_2020 = calculate_moving_average(airports_asia_2020, 10)
    
    return [(eu_2019, 'eu_2019'), (eu_2020,'eu_2020'), (us_2019,'us_2019'), (us_2020,'us_2020'), (asia_2019,'asia_2019'), (asia_2020,'asia_2020')]


def to_df(): 
    df = pd.DataFrame()
    df_list = make_list_helper()

    for d, nm in df_list:
        df = to_df_helper(df, d, nm)

    return df


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

def calculate_moving_average(dic, months):
    values = dic[0]['total'].tolist()
    values2 = dic[1]['total'].tolist()
    values3 = dic[2]['total'].tolist()

    total = [None] * months

    for i in range(months):
        tot = values[i] + values2[i] + values3[i]
        total[i] = tot

    df = pd.DataFrame(total, columns=["Total"])
    df['Total'] = pd.to_numeric(df['Total'])
    df['Average'] = df['Total'].rolling(window=12, min_periods=1).mean()

    return df

def plot_moving_average(dataset_2019, dataset_2020, name, row):
    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.subplot(3, 1, row)
    plt.plot(dataset_2019.index.values, dataset_2019['Average'], label = "2019")
    plt.plot(dataset_2020.index.values, dataset_2020['Average'], label = "2020")

    axes = plt.gca()
    bottom, top = axes.get_ylim()
    plt.ylim(bottom, top + 5000)

    plt.title(name)
    plt.xticks( np.arange(len(months)), months )
    plt.xlabel('Month')
    plt.ylabel('Rolling mean')
    plt.legend()


def main():
    plt.rcParams["figure.figsize"] = [10,6]
    fig, plots = plt.subplots(2,1)
    
    ylim = plotsub(airports_usa_2019, airportNames_usa, "Atlanta, Chicago and LA 2019", 0, 1)
    plotsub(airports_usa_2020, airportNames_usa, "Atlanta, Chicago and LA 2020", ylim, 2)
    fig.tight_layout(pad=3.0)
    plt.savefig("USASub")
    plt.close()


    fig, plots = plt.subplots(2,1)
    ylim = plotsub(airports_asia_2019, airportNames_asia, "Abu Dhabi, Tokyo and Hong Kong 2019", 0, 1)
    plotsub(airports_asia_2020, airportNames_asia, "Abu Dhabi, Tokyo and Hong Kong 2020", ylim, 2)
    fig.tight_layout(pad=3.0)
    plt.savefig("AsiaSub")
    plt.close()

    fig, plots = plt.subplots(2,1)
    ylim = plotsub(airports_europe_2019, airportNames_europe, "Paris, England and Amsterdam 2019", 0, 1)
    plotsub(airports_europe_2020, airportNames_europe, "Paris, England and Amsterdam 2020", ylim, 2)
    fig.tight_layout(pad=3.0)
    plt.savefig("EuropaSub")
    plt.close()

    df_europa_2019 = calculate_moving_average(airports_europe_2019, 12)
    df_europa_2020 = calculate_moving_average(airports_europe_2020, 10)
    
    df_usa_2019 = calculate_moving_average(airports_usa_2019, 12)
    df_usa_2020 = calculate_moving_average(airports_usa_2020, 10)
    
    df_asia_2019 = calculate_moving_average(airports_asia_2019, 12)
    df_asia_2020 = calculate_moving_average(airports_asia_2020, 10)

    fig, plots = plt.subplots(3,1)
    plot_moving_average(df_europa_2019, df_europa_2020,"Rolling Mean Europa", 1)
    plot_moving_average(df_usa_2019, df_usa_2020,"Rolling Mean USA",2)
    plot_moving_average(df_asia_2019, df_asia_2020,"Rolling Mean Asia",3)
    fig.tight_layout(pad=3.0)
    plt.savefig("RollingAverageSub")
    plt.close()


if __name__ == "__main__":
    main()