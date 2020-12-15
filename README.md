# Datacorns - BED-2056 Data Science project 2020
By: Mariel Ellingsen, Steinar Brenna Hansen and Helle Sandsdalen
> Repository for project code in course Introduction to Data Science \

In this project we examined how the pandemic impacted aviation and air quality around the world.

## Resources
### Air traffic data
The air traffic data we have used is from the [OpenSky network 2020](https://zenodo.org/record/4266937#.X9jGrdhKiMr), which provides crowdsourced air traffic data. 
- There is downloaded and used data from 2019-01-01 until 2020-10-31. 
- In our project we have chosen three different airports from the USA, Asia and Europe.
* Europe: Paris (LFPG), England (EGLL), Amsterdam (EHAM)
* USA: New York (KJFK), Chicago (KORD), Los Angeles (KLAX)
* Asia: Delhi (VIDP), Tokyo (RJTT) and Hong Kong (VHHH)

### Air quality data
The air quality data used in this survey is collected from the [World Air Quality Index project](https://aqicn.org). \
This collects data from many open quality sources around the world, including government funded sensor data and independent sensors.

### TSA data
[TSA checkpoint travel numbers for 2020 and 2019](https://www.tsa.gov/coronavirus/passenger-throughput)

## Repository
### Flights
- Under the flights folder in the repository you will find code that simplifies the original datasets, as well as code for plotting the graphs. 
- There is one data frame per airports for both 2019 and 2020. These contains total number of flights per day, as well as 7 and 30 days rolling mean. These data frames are used for visualization and analysis. 

### Air quality
- Under the air_quality folder you will find code that simplifies and plots the air quality results. 

### TSA throughput 
- The folder tsa_throughput contains the code which scrapes the web page [TSA checkpoint travel numbers for 2020 and 2019](https://www.tsa.gov/coronavirus/passenger-throughput) for the prepatory work.

### Figures
- In the firgures folder all the graphs produced by the flights, air_quality and tsa_throughput code is located. 

### Files
- In the files folder the final RMarkdown report and html page is located. This report uses the figures from the figure folder, produced by the code located in the other described folders. 

## Additional resources
- [CO2 emissions from passenger transport](https://www.eea.europa.eu/media/infographics/co2-emissions-from-passenger-transport/view)
- [Impact of COVID-19 on worldwide aviation](https://traffic-viz.github.io/scenarios/covid19.html)
- [Visualization of Air Traffic during Covid-19 Pandemic](https://towardsdatascience.com/visualization-of-air-traffic-during-covid-19-pandemic-c5941b049401)
- [The short-term impacts of COVID-19 lockdown on urban air pollution in China](https://www.nature.com/articles/s41893-020-0581-y)
- https://www.flightradar24.com/
- [AQI Basics](https://www.airnow.gov/aqi/aqi-basics/)
- [Greenhouse gas emissions from transport in Europe](https://www.eea.europa.eu/data-and-maps/indicators/transport-emissions-of-greenhouse-gases/transport-emissions-of-greenhouse-gases-12)


## Requirements for running the code
- python3 
- Pandas library (v1.1.5)
- Matplotlib library
- Numpy library

### Running the code
If you want to produce the simplified flights data sets yourself, you have have to download the data sets from the [OpenSky network 2020](https://zenodo.org/record/4266937#.X9jGrdhKiMr). 
- Put the flight data sets into the flight folder under a folder with name "dataset_flights".
- ```$ python3 cleanDailyData.py```

An example of running the code which produces 30 days rolling average plots:
- navigate to the flights folder
- ```$ python3 plotRollingAverage.py```
-  This will produce three plots, one for each continent. 
