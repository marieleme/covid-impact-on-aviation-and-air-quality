import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

LFPG_df = pd.read_csv("totalDataSets/LFPG_2019")
EGLL_df = pd.read_csv("totalDataSets/EGLL_2019")
EHAM_df = pd.read_csv("totalDataSets/EHAM_2019")
KJFK_df = pd.read_csv("totalDataSets/KJFK_2019")
KORD_df = pd.read_csv("totalDataSets/KORD_2019")
KLAX_df = pd.read_csv("totalDataSets/KLAX_2019")
VIDP_df = pd.read_csv("totalDataSets/VIDP_2019")
RJTT_df = pd.read_csv("totalDataSets/RJTT_2019")
VHHH_df = pd.read_csv("totalDataSets/VHHH_2019")

LFPG_df_2020 = pd.read_csv("totalDataSets/LFPG_2020")
EGLL_df_2020 = pd.read_csv("totalDataSets/EGLL_2020")
EHAM_df_2020 = pd.read_csv("totalDataSets/EHAM_2020")
KJFK_df_2020 = pd.read_csv("totalDataSets/KJFK_2020")
KORD_df_2020 = pd.read_csv("totalDataSets/KORD_2020")
KLAX_df_2020 = pd.read_csv("totalDataSets/KLAX_2020")
VIDP_df_2020 = pd.read_csv("totalDataSets/VIDP_2020")
RJTT_df_2020 = pd.read_csv("totalDataSets/RJTT_2020")
VHHH_df_2020 = pd.read_csv("totalDataSets/VHHH_2020")


def sum_dataframes(airpots, year, airport_names):
    total = 0
    for index, df in enumerate(airpots):
        total += df[airport_names[index] + " " + year]

    total_df = pd.DataFrame(columns = ['total'])
    total_df['total'] = total

    return total_df

def calculate_diff(df_2019, df_2020):
    diff = df_2019['total'] - df_2020['total']
    
    diff_df = pd.DataFrame(columns = ['diff'])
    diff_df['diff'] = diff

    return diff_df

def plot_global_total(df_2019, df_2020, diff_df):

    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.plot(df_2019.index.values, df_2019['total'], label="2019")
    plt.plot(df_2020.index.values, df_2020['total'], label="2020")
    plt.plot(diff_df.index.values, diff_df['diff'], label="Diff")


    plt.xticks( np.arange(len(months)), months )

    plt.ylabel('# airplanes')
    plt.xlabel('Month')
    plt.title("All airports summed")
    plt.legend()
    plt.savefig("global")


def main():
    airportNames = ["LFPG", "EGLL", "EHAM", "KJFK", "KORD", "KLAX", "VIDP", "RJTT", "VHHH"]
    airports_df_2019 = [LFPG_df, EGLL_df, EHAM_df,KJFK_df,KORD_df, KLAX_df, VIDP_df, RJTT_df,VHHH_df]
    airports_df_2020 = [LFPG_df_2020, EGLL_df_2020, EHAM_df_2020, KJFK_df_2020 ,KORD_df_2020, KLAX_df_2020, VIDP_df_2020, RJTT_df_2020,VHHH_df_2020]

    global_df_2019 = sum_dataframes(airports_df_2019, "2019", airportNames)
    global_df_2020 = sum_dataframes(airports_df_2020, "2020", airportNames)
    diff_df = calculate_diff(global_df_2019, global_df_2020)

    plot_global_total(global_df_2019, global_df_2020, diff_df)

if __name__ == "__main__":
    main()