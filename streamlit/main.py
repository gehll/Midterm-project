import streamlit as st
from data_st import get_data
from folium import Map, Marker, Icon
from streamlit_folium import st_folium
from transports import transports
import pandas as pd
from clean_raw import clean_raw


# ADD title and welcome message
st.title('My mid-term CORE project: Barcelona public transport stations')
st.text('This page shows all public transports stations in Barcelona that you can find in the following kaggle dataset: https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets')


################################################################################################################################
# At the beginning of the streamlit I want to show a map of all Barcelona
# and plot a marker for each public transport station, having each type of transport in a colour
# Bus (including day and night buses) is the type of transport that appears the most in the data
# There are so many bus stops that we will have to show only a sample of them
################################################################################################################################

rawData_params = {
    "limit": 1,
    "rawData": 0
}

rawData = []
for key in transports.keys():
    rawData.append(get_data.get_type_sample(key, rawData_params)[0])

raw_df = pd.DataFrame(rawData)
raw_df = clean_raw(raw_df)

st.subheader('Overview')

if st.checkbox('Click to see raw data'):
    st.text('Below, the data has been converted from JSON format to a dataframe \nso that each column corresponds to each field of the database.\nA filter has been performed so that there is one observation of each type of transport.')
    st.write(raw_df.sort_values(by=['Code']))


####################
# Barcelona Marker
####################


barna_coords = [41.346176, 2.168365]  # Latitude, Longitude
barna_tooltip = "City name"
barna_marker = Marker(barna_coords,
                      popup="<i>Barcelona city</i>",
                      tooltip=barna_tooltip,
                      icon=Icon(icon="home", color='black', prefix='fa'))
mapa_barna = Map(location=barna_coords, zoom_start=11, control_scale=True)
mapa_barna.add_child(barna_marker)


# Now add all public transport stations but showing only a sample of Bus

st.subheader('Sample map with all types of transports in Barcelona')


@st.cache  # Decorator to add data to cache https://docs.streamlit.io/library/get-started/create-an-app
def load_sample_data(type, params):
    return get_data.get_type_sample(type, params)


default_params = {
    "limit": 0,
    "rawData": 1
}
for key in transports.keys():
    transport_type = load_sample_data(key, default_params)
    for station in transport_type:
        Marker([station['Location']['coordinates'][1], station['Location']['coordinates'][0]],
               popup=f"<i>{station['Station']}</i>",
               tooltip=transports[key]['tooltip'],
               icon=Icon(icon=transports[key]['icon'],
                         color=transports[key]['color'], prefix='fa')).add_to(mapa_barna)


st_mapa_barna_completo = st_folium(mapa_barna)


###################################################################################################################################
# The second part of the streamlit app consist of an interactive map. The app will ask you a location (un coords or a direction),
# the type of transport that you want (max 2) and the lines that you are interested.
# This will create a geoquerie that will display the closests stations to the given location
###################################################################################################################################


st.subheader('Next, introduce a location to get the closests stations')

# TODO GET LOCATION (In coords and also a street and number)
select_type = st.multiselect('Choose how to provide the location',
                             ['coordinates', 'address'],
                             max_selections=1)

if select_type == 'address':
    location = st.text_input('Insert the address', None)
else:
    latitude = st.number_input(
        'Latitude', min_value=-90.0, max_value=90.0, value=37.067, help='Latitude is measured in degrees from the ecuator to the N or S')
    Longitude = st.number_input(
        'Longitude', min_value=-180.0, max_value=180.0, value=-2.529, help='Longitude is measured in degrees from the prime meridian to the E or W')

st.subheader('Which types of transport are you looking for?')

# TODO GET TYPE OF TRANSPORT

transport_types = st.multiselect('Choose the type of transport you want to visualize (max 2)',
                                 [key for key in transports.keys()],
                                 max_selections=2)

st.text('Which lines are you interested in?')

# TODO GET DESIRED LINES

# Get data filtered by type of transport

# Get all lines that those types of transport have

# Display multiselect with all the lines posible


# TODO plot map, centered at the location given with a marker of a person. put VIEW in 13-14


# TODO Make geoquery

# For each of the points from the geoquery, add each one of them as markers with icons and all info as in welcome map.