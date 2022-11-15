import streamlit as st
from data_st import get_data
from folium import Map, Marker, Icon
from streamlit_folium import st_folium
from transports import transports

# ADD title and welcome message
st.title('My mid-term CORE project: Barcelona public transport stations')
st.text('This page shows all public transports stations in Barcelona that you can find in the following kaggle dataset: https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets')

'''
 At the beginning of the streamlit i want to show a map of all Barcelona
and plot a marker for each public transport station, having each type of transport in a colour
'''

selected_types = st.multiselect('Choose the type of transport you want to visualize (max 2)',
                                [key for key in transports.keys()],
                                max_selections=2)


# Barcelon map

barna_coords = [41.346176, 2.168365] # Latitude, Longitude
barna_tooltip = "City name"
barna_marker = Marker(barna_coords, 
                        popup="<i>Barcelona city</i>", 
                        tooltip=barna_tooltip,
                        icon=Icon(icon="home", color='black', prefix='fa'))
mapa_barna = Map(location=barna_coords, zoom_start=11)
mapa_barna.add_child(barna_marker)

# Now add all public transport stations that haven been selected with the multiselect

colors = ['blue', 'green']

i = 0
for key in selected_types:
    transport_type = get_data.get_transport_type(key)
    for station in transport_type:
        Marker([station['Location']['coordinates'][1], station['Location']['coordinates'][0]], 
                popup=f"<i>{station['Station']}</i>", 
                tooltip=transports[key]['tooltip'],
                icon=Icon(icon=transports[key]['icon'], 
                        color=colors[i], prefix='fa')).add_to(mapa_barna)
    i += 1

st_mapa_barna_completo = st_folium(mapa_barna)


'''
The second part of the streamlit app consist of an interactive map. The app will ask you a location (un coords or a direction),
the type of transport that you want (max 2) and the lines that you are interested.

This will create a geoquerie that will display the closests stations to the given location
'''

st.text('Next, introduc a location to get the closests stations')

# TODO GET LOCATION (In coords and also a street and number)



st.text('Which types of transport are you looking for?')

# TODO GET TYPE OF TRANSPORT


st.text('Which lines are you interested in?')

# TODO GET DESIRED LINES

