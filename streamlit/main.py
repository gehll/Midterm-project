import streamlit as st
from data_st import get_data
from folium import Map, Marker, Icon
from streamlit_folium import st_folium
from transports import transports
import pandas as pd
from clean_raw import clean_raw
from useful.get_lines import get_lines
from utils import create_marker
from create_pdf import PDF
import io
from PIL import Image


# ADD title and welcome message
st.title('My mid-term CORE project: Barcelona public transport stations')
st.text('This page shows a variety of public transports stations in Barcelona that you can \nfind in the following kaggle dataset: \nhttps://www.kaggle.com/datasets/xvivancos/barcelona-data-sets')


#########################################################
###
# Display a sample of the data as a dataframe
###
#########################################################


st.subheader('Overview')

if st.checkbox('Click to see raw data'):

    # Parameters of get_type_sample(). "limit"=1 gets only 1 observation of each transport type
    # "rawData=0" means that we get 1 observation also for "Bus" type. "rawData=1" is to sample 50
    # observations of the type "Bus"

    rawData_params = {
        "limit": 1,
        "rawData": 0
    }

    rawData = []  # List that will contain the sample data that will be displayed as a dataframe
    for key in transports.keys():
        rawData.append(get_data.get_type_sample(key, rawData_params)[0])

    raw_df = pd.DataFrame(rawData)
    raw_df = clean_raw(raw_df)

    st.text('Below, the data has been converted from JSON format to a dataframe \nso that each column corresponds to each field of the database.\nA filter has been performed so that there is one observation of each type of transport.')
    st.write(raw_df.sort_values(by=['Code']))


################################################################################################################################
# First, I want to show a map of all Barcelona
# and plot a marker for each type of public transport, having each type of transport in a colour.
# Bus (including day and night buses) is the type of transport that appears the most in the data.
# There are so many bus stops that we will have to show only a sample of them
################################################################################################################################


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


# Now we set the params so that we sample only 50 bus stations but all from the other types
default_params = {
    "limit": 0,
    "rawData": 1
}

for key in transports.keys():
    transport_type = load_sample_data(key, default_params)
    for station in transport_type:
        marker = create_marker(station, key)
        mapa_barna.add_child(marker)

st_mapa_barna_completo = st_folium(mapa_barna)


###################################################################################################################################
# The second part of the streamlit app consist of an interactive map. The app will ask you a location (in coordinates),
# the type of transport that you want (max 2) and the lines that you are interested.
# This will create a geoquerie that will display the closests stations to the given location
###################################################################################################################################


st.subheader('Next, introduce a location to get the closest stations')

location = []
if st.checkbox('Check the box if you want to seach for the nearest stations',
               value=False):
    latitude = st.number_input(
        'Latitude', min_value=-90.0, max_value=90.0, help='Latitude is measured in degrees from the ecuator to the N or S')
    longitude = st.number_input(
        'Longitude', min_value=-180.0, max_value=180.0, help='Longitude is measured in degrees from the prime meridian to the E or W')
    location.append(str(latitude))
    location.append(str(longitude))

    st.subheader('What types of transport are you looking for?')

    # Choose the type of transport

    transport_types = st.multiselect('Choose the type of transport you want to visualize (max 2)',
                                     [key for key in transports.keys()],
                                     max_selections=2)

    st.text('Which lines are you interested in?')

    # Get the lines you are looking for

    # --- First, get data filtered by the previous types to then get all lines
    # --- for those types of transport

    transport_data = [get_data.get_transport_type(
        type) for type in transport_types]  # List of lists with JSON documents

    # Get all lines that those types of transport have

    lines = get_lines(transport_data)

    # Display multiselect to choose from all available lines

    selected_lines = st.multiselect('Choose the lines that you want to look for',
                                    [line for line in lines])

    # --- GEOQUERY to get closest stations

    # List to store filtered stations for each type of transport
    geo_data = []
    for transport in transport_types:  # For each type of transport get the closest stations to given coordinates

        geo_params = {
            "location": location,
            "type": transport,
            "lines": selected_lines
        }

        closest = get_data.make_geoquery(geo_params)
        geo_data.append(closest)

    # If we have coordinates, transport type and lines, plot the map
    if location and transport_types and selected_lines:

        coords = location  # Latitude, Longitude
        coords_tooltip = "Me!"
        coords_marker = Marker(coords,
                               popup=f"<i>{location}</i>",
                               tooltip=coords_tooltip,
                               icon=Icon(icon="user", color='black', prefix='fa'))
        mapa_coords = Map(location=coords, zoom_start=12, control_scale=True)
        mapa_coords.add_child(coords_marker)

        # For each of the points from the geoquery, add each one of them as markers with icons and all info as in welcome map.

        for idx, type in enumerate(geo_data):
            for doc in type:
                marker = create_marker(doc, transport_types[idx])
                mapa_coords.add_child(marker)

        st_mapa_coords_completo = st_folium(mapa_coords)


########################################################################################
########################################################################################
###
# The last thing we are going to incorporate to the streamlit app is a button to  give
# the option to download the map as a PDF and/or send it via e-amail
########################################################################################
########################################################################################

st.subheader('Downdload the results as PDF')

# --- Checkout to download PDF

download = st.checkbox('Download as PDF')

if download:

    # Instantiation of inherited class
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)

    img_data = mapa_coords._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save('coords.png')

    pdf.output('CORE.pdf', 'F')

    # Button to download pdf

    # Checkbox to give the option to send a copy via email as well

    # If yes, text input for the email (PUT STRIP)
    # Another text input to double-check email
    # Check if email is correct and SEND
