import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates
import air_quality.air_quality_parser as aqp
import flights.airport as air


df_aq = aqp.combined_region_dfs(7)
df_at = air.to_df()

# print(df_aq)
# print(df_at)

def get_aq_line(region):
    for regions, city_df in df_aq.items():
        if region == regions:
            return (city_df,[regions + '-mean-2019', regions + '-mean-2020'])

city_df, lines_aq = get_aq_line('eu')
# ax.xaxis.set_major_locator(dates.MonthLocator(interval=1))

df_aq_to_oct = city_df[lines_aq[1]]
df_aq_to_oct = df_aq_to_oct[:304]


print(df_aq_to_oct)
