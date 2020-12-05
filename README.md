# sqlalchemy-challenge
 
## Surf's Up

### included
1. [CT_climate_starter.ipynb](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/CT_climate_starter.ipynb)
2. [app.py](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/app.py)
3. [Resources folder](https://github.com/tratnikc/sqlalchemy-challenge/tree/main/Resources)
   * hawaii.sqlite
   * hawaii_stations.csv
   * hawaii_measurements.csv
4. Outputs in [Images folder](https://github.com/tratnikc/sqlalchemy-challenge/tree/main/Images)
   * [Precipitation analysis](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/precipitation.png)
   * [Summary statistics](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/summary_statistics.png)
   * [Stations histogram](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/histogram.png)
   * [Trip Average Temperature](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/trip_avg_temp.png)
   * [Daily normals](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/daily_normals.png)

### Requirements
#### Climate Analysis and Exploration
* Use SQLAlchemy to connect to sqlite database
* Use SQLAlchemy to reflect tables into classes and save reference to those classes

##### Precipitation Analysis
* Design a query to retrieve the last 12 months of precipitation data
* Load the query results into a Pandas DataFrame
* Plot the results using DataFrame plot method
* Use Pandas to print the summary statistics for the precipitation data

##### Station Analysis
* Design a query to calculate the total number of stations
* Design a query to find the most active stations
* Design a query to retrieve the last 12 months of temperature observations data (TOBS)
* Plot the results as a histogram with bins=12

#### Climate App
* Create Routes
   * /  
        * home page; list all routes that are available
   * /api/v1.0/precipitation  
        * return the JSON representation of dictionary from query results using date as key and prcp as value
   * /api/v1.0/stations
        * return a JSON list pf stations from the dataset
   * /api/v1.0/tobs
        * return a JSON list of tobs for the previous year for the most active station
   * <p>/api/v1.0/&lt;start&gt;</p>
        * return TMIN, TAVG, TMAX for a all dates greater than and equal to the start date
   * <p>/api/v1.0/&lt;start&gt;/&lt;end&gt;</p>
        * return TMIN, TAVG, TMAX for a all dates between start date and end date, inclusive

### Analysis
#### Precipitation Analysis  
![Precipitation Analysis](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/precipitation.png)
#### Summary Statistics  
![Summary Statistics](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/summary_statistics.png)
#### Stations Histogram  
![stations historgram](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/histogram.png)
#### Temperature Analysis
![temperature analysis](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/trip_avg_temp.png)
#### Daily Rainfall Average
![daily rainfall average](https://github.com/tratnikc/sqlalchemy-challenge/blob/main/Images/daily_normals.png)

