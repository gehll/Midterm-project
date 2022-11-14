import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objs as go
from data.get_data import get_collection, get_transport_type

st.title('My mid-term CORE project: Barcelona public transport stations')
st.text('This page shows all public transports stations in Barcelona that you can find in the following kaggle dataset: https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets')
