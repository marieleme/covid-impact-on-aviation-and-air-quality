import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates
import air_quality.air_quality_parser as aqp
import flights.Global30Rolling as air

def get_dataframes(cont):
    df_aq = aqp.combined_region_dfs(7)
    df_19, df_20= air.sum_df(cont)
    return df_aq, df_20

def get_aq_line(region, df_aq):
    for regions, city_df in df_aq.items():
        if region == regions:
            return (city_df,[regions + '-mean-2019', regions + '-mean-2020'])

def extract_air_quality_data(cont, df_aq):
    city_df, lines_aq = get_aq_line(cont, df_aq)

    df_aq_to_oct= pd.DataFrame()
    df_aq_to_oct[cont] = city_df[lines_aq[1]]
    df_aq_to_oct = df_aq_to_oct[:304]

    return df_aq_to_oct

def plot(cont, df1, df2):
    fig,ax = plt.subplots()

    line = ax.plot(df1['total'], label="Aviation 2020", color="black")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of airplanes",color="black")

    ax2=ax.twinx()
    scatter = ax2.scatter( df2.index, df2[cont], label="Air quality 2020", color="purple")
    ax2.set_ylabel("Air quality",color="purple")

    ax.xaxis.set_major_locator(dates.MonthLocator(interval=1))
    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
    ax.set_xticks(ax.get_xticks().tolist()[0:11])
    ax.set_xticklabels(months)

    plt.legend([line[0], scatter], ['Aviation', 'Air quality'])
    plt.title("Aviation and air quality data with 30 days rolling average, Asia 2020")
    plt.savefig('combined_asia')

def main(cont):
    df_aq, df_aviation = get_dataframes(cont)
    df_airquality = extract_air_quality_data(cont, df_aq)
    plot(cont, df_aviation, df_airquality)


if __name__ == "__main__":
    main('asia')