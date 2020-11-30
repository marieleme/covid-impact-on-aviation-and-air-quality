import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np 

LFPG_df = pd.read_csv("simpleData/LFPG_2019")
EGLL_df = pd.read_csv("simpleData/EGLL_2019")
EHAM_df = pd.read_csv("simpleData/EHAM_2019")
KATL_df = pd.read_csv("simpleData/KATL_2019")
KORD_df = pd.read_csv("simpleData/KORD_2019")
KLAX_df = pd.read_csv("simpleData/KLAX_2019")
OMAA_df = pd.read_csv("simpleData/OMAA_2019")
RJTT_df = pd.read_csv("simpleData/RJTT_2019")
VHHH_df = pd.read_csv("simpleData/VHHH_2019")

LFPG_df_2020 = pd.read_csv("simpleData/LFPG_2020")
EGLL_df_2020 = pd.read_csv("simpleData/EGLL_2020")
EHAM_df_2020 = pd.read_csv("simpleData/EHAM_2020")
KATL_df_2020 = pd.read_csv("simpleData/KATL_2020")
KORD_df_2020 = pd.read_csv("simpleData/KORD_2020")
KLAX_df_2020 = pd.read_csv("simpleData/KLAX_2020")
OMAA_df_2020 = pd.read_csv("simpleData/OMAA_2020")
RJTT_df_2020 = pd.read_csv("simpleData/RJTT_2020")
VHHH_df_2020 = pd.read_csv("simpleData/VHHH_2020")

airports_europe_2019 = [LFPG_df, EGLL_df, EHAM_df]
airports_usa_2019 = [KATL_df, KORD_df, KLAX_df]
airports_asia_2019 = [OMAA_df, RJTT_df, VHHH_df]

airports_europe_2020 = [LFPG_df_2020, EGLL_df_2020, EHAM_df_2020]
airports_usa_2020 = [KATL_df_2020, KORD_df_2020, KLAX_df_2020]
airports_asia_2020 = [OMAA_df_2020, RJTT_df_2020, VHHH_df_2020]

airportNames_europe = ["LFPG", "EGLL", "EHAM"]
airportNames_usa = ["KATL", "KORD", "KLAX"]
airportNames_asia = ["OMAA", "RJTT", "VHHH"]

def plot(airpors_region, airportnames, region, year):

    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    counter = 0
    for i in airpors_region:
        plt.plot(i.index.values , i['total'], label =airportnames[counter])
        counter += 1

    plt.xticks( np.arange(len(months)), months )
    plt.xlabel('Month')
    plt.ylabel('# airplanes')
    plt.title(region)
    plt.rcParams["figure.figsize"] = [10,6]
    plt.legend()
    plt.savefig(region)
    plt.close()


def calculate_moving_average(dic, months):
    values = dic[0]['total'].tolist()
    values2 = dic[1]['total'].tolist()
    values3 = dic[2]['total'].tolist()

    total = [None] * months

    for i in range(months):
        tot = values[i] + values2[i] + values3[i]
        total[i] = tot

    print(total)
    df = pd.DataFrame(total, columns=["Total"])
    df['Total'] = pd.to_numeric(df['Total'])
    df['Average'] = df['Total'].rolling(window=12, min_periods=1).mean()

    return df

def plot_moving_average(dataset_2019, dataset_2020, name):
    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.plot(dataset_2019.index.values, dataset_2019['Average'], label = "2019")
    plt.plot(dataset_2020.index.values, dataset_2020['Average'], label = "2020")


    plt.xticks( np.arange(len(months)), months )
    plt.xlabel('Month')
    plt.ylabel('Rolling mean')
    plt.title(name)
    plt.rcParams["figure.figsize"] = [10,6]
    plt.legend()
    plt.savefig(name)
    plt.close()


def main():
    plot(airports_europe_2019, airportNames_europe, "Europa2019", "2019")
    plot(airports_europe_2020, airportNames_europe, "Europa2020", "2020")

    plot(airports_usa_2019, airportNames_usa, "USA2019", "2019")
    plot(airports_usa_2020, airportNames_usa, "USA2020", "2020")

    plot(airports_asia_2019, airportNames_asia, "Asia2019", "2019")
    plot(airports_asia_2020, airportNames_asia, "Asia2020", "2020")

    df_europa_2019 = calculate_moving_average(airports_europe_2019, 12)
    df_europa_2020 = calculate_moving_average(airports_europe_2020, 10)
    
    df_usa_2019 = calculate_moving_average(airports_usa_2019, 12)
    df_usa_2020 = calculate_moving_average(airports_usa_2020, 10)
    
    df_asia_2019 = calculate_moving_average(airports_asia_2019, 12)
    df_asia_2020 = calculate_moving_average(airports_asia_2020, 10)

    plot_moving_average(df_europa_2019, df_europa_2020,"RollingMeanEuropa")
    plot_moving_average(df_usa_2019, df_usa_2020,"RollingMeanUSA")
    plot_moving_average(df_asia_2019, df_asia_2020,"RollingMeanAsia")


if __name__ == "__main__":
    main()