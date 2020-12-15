import pandas as pd

def parse_all(airports, file, airportNames, month):
    df = pd.read_csv(file, usecols=['origin', 'destination'])

    for row in df.itertuples():
        if row.origin in airportNames:
            if month not in airports[row.origin]:
                airports[row.origin][month] = 0
            
            airports[row.origin][month] += 1

        if row.destination in airportNames:
            
            if month not in airports[row.destination]:
                airports[row.destination][month] = 0
            
            airports[row.destination][month] += 1

    return airports

def convert_to_csv(airports, year):
    for airport, dict in airports.items():
        df = pd.DataFrame.from_dict(airports[airport], orient='index', columns=[airport + " " + year])

        if(year == "2020"):
            df.loc["Nov"] = [0]
            df.loc["Dec"] = [0]

        df.to_csv("totalDataSets/" + airport + "_" + year)

def main():
    airportNames = ["LFPG", "EGLL", "EHAM", "KJFK", "KORD", "KLAX", "VIDP", "RJTT", "VHHH"]
    airports = {airport : {} for airport in airportNames}

    airports = parse_all(airports, "dataset_flights/flightlist_20190101_20190131.csv", airportNames, "Jan")
    airports = parse_all(airports, "dataset_flights/flightlist_20190201_20190228.csv", airportNames, "Feb")
    airports = parse_all(airports, "dataset_flights/flightlist_20190301_20190331.csv", airportNames, "Mar")
    airports = parse_all(airports, "dataset_flights/flightlist_20190401_20190430.csv", airportNames, "Apr")
    airports = parse_all(airports, "dataset_flights/flightlist_20190501_20190531.csv", airportNames, "May")
    airports = parse_all(airports, "dataset_flights/flightlist_20190601_20190630.csv", airportNames, "Jun")
    airports = parse_all(airports, "dataset_flights/flightlist_20190701_20190731.csv", airportNames, "Jul")
    airports = parse_all(airports, "dataset_flights/flightlist_20190801_20190831.csv", airportNames, "Aug")
    airports = parse_all(airports, "dataset_flights/flightlist_20190901_20190930.csv", airportNames, "Sep")
    airports = parse_all(airports, "dataset_flights/flightlist_20191001_20191031.csv", airportNames, "Oct")
    airports = parse_all(airports, "dataset_flights/flightlist_20191101_20191130.csv", airportNames, "Nov")
    airports = parse_all(airports, "dataset_flights/flightlist_20191201_20191231.csv", airportNames, "Dec")

    convert_to_csv(airports, "2019")
    airports = {airport : {} for airport in airports}

    airports = parse_all(airports, "dataset_flights/flightlist_20200101_20200131.csv", airportNames, "Jan")
    airports = parse_all(airports, "dataset_flights/flightlist_20200201_20200229.csv", airportNames, "Feb")
    airports = parse_all(airports, "dataset_flights/flightlist_20200301_20200331.csv", airportNames, "Mar")
    airports = parse_all(airports, "dataset_flights/flightlist_20200401_20200430.csv", airportNames, "Apr")
    airports = parse_all(airports, "dataset_flights/flightlist_20200501_20200531.csv", airportNames, "Mai")
    airports = parse_all(airports, "dataset_flights/flightlist_20200601_20200630.csv", airportNames, "Jun")
    airports = parse_all(airports, "dataset_flights/flightlist_20200701_20200731.csv", airportNames, "Jul")
    airports = parse_all(airports, "dataset_flights/flightlist_20200801_20200831.csv", airportNames, "Aug")
    airports = parse_all(airports, "dataset_flights/flightlist_20200901_20200930.csv", airportNames, "Sep")
    airports = parse_all(airports, "dataset_flights/flightlist_20201001_20201031.csv", airportNames, "Oct")

    convert_to_csv(airports, "2020")

if __name__ == "__main__":
    main()    