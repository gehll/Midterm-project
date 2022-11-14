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

transports = {'Bus': ['K014', 'K015'],
    'Bus_airport': ['K016'],
    'Bus_station': ['K017'],
    'Metro': ['K001'],
    'Railway': ['K002'],
    'Renfe': ['K003'],
    'Airport_train': ['K004'],
    'Maritime_station': ['K008'],
    'Funicular': ['K009'],
    'Cableway': ['K010'],
    'Tramvia': ['K011'],
    }

transports_icons = {'Bus': 'bus',
    'Bus_airport': 'bus',
    'Bus_station': 'bus',
    'Metro': 'train-tunnel',
    'Railway': 'train-track',
    'Renfe': 'train',
    'Airport_train': 'train-subway',
    'Maritime_station': 'ship',
    'Funicular': 'up-from-line',
    'Cableway': 'cable-car',
    'Tramvia': 'train-tram',
    }

transports_tooltip = {'Bus': 'Bus',
    'Bus_airport': 'Bus-airport',
    'Bus_station': 'Bus-station',
    'Metro': 'Subway',
    'Railway': 'Railway',
    'Renfe': 'RENFE',
    'Airport_train': 'Airport-train',
    'Maritime_station': 'Maritime-station',
    'Funicular': 'Funicular',
    'Cableway': 'Cableway',
    'Tramvia': 'Tramvia',
    }

transports_colors = {'Bus': 'red',
    'Bus_airport': 'red',
    'Bus_station': 'red',
    'Metro': 'green',
    'Railway': 'green',
    'Renfe': 'green',
    'Airport_train': 'green',
    'Maritime_station': 'blue',
    'Funicular': 'beige',
    'Cableway': 'purple',
    'Tramvia': 'orange',
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
                tooltip=transports_tooltip[key],
                icon=Icon(icon=transports_icons[key], 
                        color=transports_colors[key])).add_to(mapa_barna)

st_mapa_barna_completo = st_folium(mapa_barna)
