import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la página
st.header("Datos de anuncios de coches")

car_data = pd.read_csv('./vehicles_us.csv') # Leemos los datos

# Creamos una casilla de selección, para elegir histograma y gráfico de dispersión
build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_histogram: # Si la casilla de histograma está seleccionada
  st.write('Construir un histograma para la columna Odómetro')
  
  # Creamos histograma
  fig = px.histogram(car_data, x='odometer')
  
  # Mostramos gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)

if build_scatter: # Si la casilla de gráfico de dispersión está seleccionada
  st.write('Construir un gráfico de dispersión para las columnas Odómetro y Precio')
  
  # Creamos gráfico de dispersión
  fig = px.scatter(car_data, x='odometer', y='price')
  
  # Mostramos gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)
  