import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objs as go
from data_st import get_data
from folium import Map, Marker, Icon
from streamlit_folium import st_folium

st.title('My mid-term CORE project: Barcelona public transport stations')
st.text('This page shows all public transports stations in Barcelona that you can find in the following kaggle dataset: https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets')

'''
 At the beginning of the streamlit i want to show a map of all Barcelona
and plot a marker for each public transport station, having each type of transport in a colour
'''

transports = {'Bus': {'Code': ['K014', 'K015'], 'icon': 'bus', 'tooltip': 'Bus'},
    'Bus_airport': {'Code':['K016'], 'icon': 'bus', 'tooltip': 'Bus-airpot'},
    'Bus_station': {'Code':['K017'], 'icon': 'bus', 'tooltip': 'Bus-station'},
    'Metro': {'Code':['K001'], 'icon': 'subway', 'tooltip': 'Subway'},
    'Railway': {'Code':['K002'], 'icon': 'train', 'tooltip': 'Railway'},
    'Renfe': {'Code':['K003'], 'icon': 'train', 'tooltip': 'RENFE'},
    'Airport_train': {'Code':['K004'], 'icon': 'train', 'tooltip': 'Airport-train'},
    'Maritime_station': {'Code':['K008'], 'icon': 'ship', 'tooltip': 'Maritime-station'},
    'Funicular': {'Code':['K009'], 'icon': 'arrow-up', 'tooltip': 'Funicular'},
    'Cableway': {'Code':['K010'], 'icon': 'square-o', 'tooltip': 'Cableway'},
    'Tramvia': {'Code':['K011'], 'icon': 'minus', 'tooltip': 'Tramvia'}
    }

selected_types = st.multiselect('Choose the type of transport you want to visualize (max 2)',
                                [key for key, _ in transports.items()],
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