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

transports = {'Bus': {'Code': ['K014', 'K015'], 'icon': 'bus', 'tooltip': 'Bus', 'color':'red'},
    'Bus_airport': {'Code':['K016'], 'icon': 'bus', 'tooltip': 'Bus-airpot', 'color':'red'},
    'Bus_station': {'Code':['K017'], 'icon': 'bus', 'tooltip': 'Bus-station', 'color':'red'},
    'Metro': {'Code':['K001'], 'icon': 'train-tunnel', 'tooltip': 'Subway', 'color':'green'},
    'Railway': {'Code':['K002'], 'icon': 'train-track', 'tooltip': 'Railway', 'color':'green'},
    'Renfe': {'Code':['K003'], 'icon': 'train', 'tooltip': 'RENFE', 'color':'green'},
    'Airport_train': {'Code':['K004'], 'icon': 'train-subway', 'tooltip': 'Airport-train', 'color':'green'},
    'Maritime_station': {'Code':['K008'], 'icon': 'ship', 'tooltip': 'Maritime-station', 'color':'blue'},
    'Funicular': {'Code':['K009'], 'icon': 'up-from-line', 'tooltip': 'Funicular', 'color':'beige'},
    'Cableway': {'Code':['K010'], 'icon': 'cable-car', 'tooltip': 'Cableway', 'color':'purple'},
    'Tramvia': {'Code':['K011'], 'icon': 'train-tram', 'tooltip': 'Tramvia', 'color':'orange'}
    }

barna_coords = [41.346176, 2.168365] # Latitude, Longitude
barna_tooltip = "City name"
barna_marker = Marker(barna_coords, 
                        popup="<i>Barcelona city</i>", 
                        tooltip=barna_tooltip,
                        icon=Icon(icon="city"))
mapa_barna = Map(location=barna_coords, zoom_start=11)
mapa_barna.add_child(barna_marker)

# Now add all public transport stations

for key, value in transports.items():
    transport_type = get_data.get_transport_type(key)
    for station in transport_type:
        Marker([station['Location']['coordinates'][1], station['Location']['coordinates'][0]], 
                popup=f"<i>{station['Station']}</i>", 
                tooltip=transports[key]['tooltip'],
                icon=Icon(icon=transports[key]['icon'], 
                        color=transports[key]['color'])).add_to(mapa_barna)

st_mapa_barna_completo = st_folium(mapa_barna)
