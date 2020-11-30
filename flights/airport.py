from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np 
# https://zenodo.org/record/4266938#.X8AO1HVKg5k

# Paris	 = LFPG
# London = EGLL
# Amsterdam = EHAM
# 
# Atlanta - KATL
# Chicago - KORD
# Los Angeles - KLAX 
# 
# Shanghai - ZSPD
# Tokyo - RJTT
# Beijing - ZBAA  (5,6)

# RKSI - SEOUL
# VHHH - hong kong 
# WSSS - Singapore
airports_europe_2019 = {"LFPG": {}, "EGLL":  {}, "EHAM": {}}
airports_usa_2019 = {"KATL": {}, "KORD": {}, "KLAX": {}}
airports_asia_2019 = {"OMAA": {}, "RJTT":{}, "VHHH":{}}

airports_europe_2020 = {"LFPG": {}, "EGLL":  {}, "EHAM": {}}
airports_usa_2020 = {"KATL": {}, "KORD": {}, "KLAX": {}}
airports_asia_2020 = {"OMAA": {}, "RJTT":{}, "VHHH":{}}

airportNames_europe = ["LFPG", "EGLL", "EHAM"]
airportNames_usa = ["KATL", "KORD", "KLAX"]
airportNames_asia = ["OMAA", "RJTT", "VHHH"]


def read_csv(filename, airports_europe,airports_usa,airports_asia, month):
    df = pd.read_csv(filename, usecols=[5,6])

    for (columnName, columnData) in df.iteritems():
        for i in columnData.values:
            if i in airportNames_europe:
                if month not in airports_europe[i]:
                        airports_europe[i][month] = 0
                airports_europe[i][month] += 1
            elif i in airportNames_usa:
                if month not in airports_usa[i]:
                        airports_usa[i][month] = 0
                airports_usa[i][month] += 1
            elif i in airportNames_asia:
                if month not in airports_asia[i]:
                        airports_asia[i][month] = 0
                airports_asia[i][month] += 1



def plot(airports, region, airportNames, year):
    if(year == "2019"):
        y = [1,2,3,4,5,6,7,8,9,10,11,12]
        months = ["","Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    else:      
        y = [1, 2, 3, 4, 5,6,7,8,9,10]
        months = ["","Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct"]

    for i in airportNames:
        airport = airports[i]
        plt.plot(y,list(airport.values()), label=i)
    
    plt.xticks( np.arange(len(months)), months )
    plt.xlabel('Month')
    plt.ylabel('# airplanes')
    plt.title(region)
    plt.rcParams["figure.figsize"] = [10,6]
    plt.legend()
    plt.savefig(region)
    plt.close()

def calculate_moving_average(dic, airportNames):
    values = list(dic[airportNames[0]].values())
    values2= list(dic[airportNames[1]].values())
    values3= list(dic[airportNames[2]].values())

    total = []

    for i in range(len(values)):
        tot = values[i] + values2[i] + values3[i]
        total.append(tot)

    moving_average = []

    for i in range(len(total)):
        moving = total[i] + total[i-1]
        if i != 0:
            moving_average.append(moving/i)

    return moving_average    


def plot_moving_avrg(list_2019, list_2020, region):
    y = [1,2,3,4,5,6,7,8,9,10,11,12]

    print(list_2019)
    plt.plot(y, list_2019)
    plt.plot(y[10:], list_2020)
    plt.xlabel('Month')
    plt.ylabel('# airplanes')
    plt.title(region + " 12-month moving right average")
    
    plt.legend()
    plt.savefig(region + " 12-month moving right average")
    plt.close()

read_csv("flightlist_20190101_20190131.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Jan")
read_csv("flightlist_20190201_20190228.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Feb")
read_csv("flightlist_20190301_20190331.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Mar")
read_csv("flightlist_20190401_20190430.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Apr")
read_csv("flightlist_20190501_20190531.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "May")
read_csv("flightlist_20190601_20190630.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Jun")
read_csv("flightlist_20190701_20190731.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Jul")
read_csv("flightlist_20190801_20190831.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Aug")
read_csv("flightlist_20190901_20190930.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Sep")
read_csv("flightlist_20191001_20191031.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Oct")
read_csv("flightlist_20191101_20191130.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Nov")
read_csv("flightlist_20191201_20191231.csv", airports_europe_2019, airports_usa_2019,airports_asia_2019, "Dec")


# read_csv("flightlist_20200101_20200131.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Jan")
# read_csv("flightlist_20200201_20200229.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Feb")
# read_csv("flightlist_20200301_20200331.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Mar")
# read_csv("flightlist_20200401_20200430.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Apr")
# read_csv("flightlist_20200501_20200531.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "May")
# read_csv("flightlist_20200601_20200630.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Jun")
# read_csv("flightlist_20200701_20200731.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Jul")
# read_csv("flightlist_20200801_20200831.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Aug")
# read_csv("flightlist_20200901_20200930.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Sep")
# read_csv("flightlist_20201001_20201031.csv", airports_europe_2020, airports_usa_2020,airports_asia_2020, "Oct")


print(airports_europe_2019)
print(airports_usa_2019)
print(airports_asia_2019)

plot(airports_europe_2019, "Europe", airportNames_europe,"2019")
plot(airports_usa_2019, "USA", airportNames_usa,"2019")
plot(airports_asia_2019, "Asia", airportNames_asia,"2019")

# plot(airports_europe_2020, "Europe 2020", airportNames_europe,"2020")
# plot(airports_usa_2020, "USA 2020", airportNames_usa, "2020")
# plot(airports_asia_2020, "Asia 2020", airportNames_asia, "2020")

moving_avg_europ_2019 = calculate_moving_average(airports_europe_2019, airportNames_europe)
moving_avg_europ_2020 = calculate_moving_average(airports_europe_2020, airportNames_europe)

moving_avg_usa_2019 = calculate_moving_average(airports_usa_2019, airportNames_usa)
moving_avg_usa_2020 = calculate_moving_average(airports_usa_2020, airportNames_usa)

moving_avg_asia_2019 = calculate_moving_average(airports_asia_2019, airportNames_asia)
moving_avg_asia_2020 = calculate_moving_average(airports_asia_2020, airportNames_asia)

plot_moving_avrg(moving_avg_asia_2019, moving_avg_asia_2020, "Asia")