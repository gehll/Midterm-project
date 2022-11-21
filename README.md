# Midterm-project

![](tp_barna.png)

Author: Gonzalo España-Heredia Llanza

This repo contains all code needed to replicate my personal mid-term project of the Big Data & ML bootcamp.

The repo has 3 main parts:
- Data cleaning
- API
- Streamlit app

## Launch the project

From the cli in the path of the repository:

**To launch the API**

```bash
cd api
./run_api-develop.sh
```

**o laucnh the streamlit app**

```bash
cd streamlit
./run_streamlit-develop.sh
```

## Data cleaning

The data used comes from [kaggle](https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets) from a dataset with data about the city of Barcelona. For this project only two data files are needed: transports.csv and bus_stops.csv.

**transports.csv** contains data about different types of public transports (subway, railway, cableway, tramvia, etc) and **bus_stops.csv** contains data about the different types of bus stations (day bus, night bus, airport bus, bus stations). 

During the cleaning, the goal was to concatenate both datasets so it was necessary to rename columns, have a consistent format across both datasets, clean data and create new columns. To access the data through the API, the data was stored in Mongodb Atlas, mainly because the goal was to make geoqueries later on the streamlit and, thus it is better to work with mongo than with a relational database. After the data was cleaned, a blank collection was filled with the clean data, this collection is called **geo_transports**.

## API

The API is used as the connection between Mongodb Atlas and the streamlit app. There are several endpoints to access the data in the collection (geo_transports). All the endpoints can be found at `api/routers/endpoints.py`.

## Streamlit

The streamlit app consists of two main parts:
- Overview
- Query map

#### Overview

At the beginning of the streamlit, you can see a map of the city of Barcelon with different markers that display station of all the transport types in the data. This maps shows only a sample of all stations. Also, before the map, you can find a sample of the data by clicking on a checkbox.

#### Query map

The next and last part is a map that shows the closests transport stations based on a query. The query asks you to enter some coordinates, the types of transport you would like to filter (maximum 2 types) and the desired lines from those types of transport. When filtering for the lines, the list can be quite long, especially if you select *Bus*. The reason of showing a list and choosing from the list instead of asking for the desired lines with text input, is because I suppose that most of the people don't know the names of the lines for each type of transport in Barcelona.

After introducing the query parameters, a geoquery is made to display a map with the closest stations where your desired lines pass through. You will get the 5 closest stationf for each type of transports that you select.
