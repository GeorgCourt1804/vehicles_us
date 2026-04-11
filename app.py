import pandas as pd
import plotly.express as px
import streamlit as st

# Funciones reutilizables

def cargar_datos(ruta:str):
  """Cargar un archivo CSV y retornar un DataFrame"""
  return pd.read_csv(ruta)

def mostrar_histograma(df: pd.DataFrame, columna:str, titulo:str=None):
  """
  Muestra un histograma interactivo en Streamlit.
  
  Args:
      df: DataFrame con los datos.
      columna: Nombre de la columna a graficar.
      titulo: Texto descriptivo que aparece sobre el gráfico.
  """
  
  if titulo:
    st.write(titulo)
  fig = px.histogram(df, x=columna)
  st.plotly_chart(fig, use_container_width=True)
  
def mostrar_dispersion(df: pd.DataFrame, col_x:str, col_y:str, titulo:str=None):
  """
  Muestra un gráfico de dispersión interactivo en Streamlit.
  
  Args:
      df: DataFrame con los datos.
      col_x: Columna para el eje X.
      col_y: Columna para el eje Y.
      titulo: Texto descriptivo que aparece sobre el gráfico.
  """
  
  if titulo:
    st.write(titulo)
  fig = px.scatter(df, x=col_x, y=col_y)
  st.plotly_chart(fig, use_container_width=True)
  
def mostrar_checkbox_grafico(label:str, accion):
  """
  Crea un checkbox y ejecuta la función `acción` si está marcado.
  
  Args:
      label: Texto que aparece junto al checkbox.
      accion: Función sin argumentos a ejecutar cuando el checkbox está activo.
  """
  
  if st.checkbox(label):
    accion()
    
# Aplicación principal

def main():
  st.header("Datos de anuncios de coches")
  
  car_data = cargar_datos('./vehicles_us.csv')
  
  mostrar_checkbox_grafico(
    label='Construir histograma',
    accion=lambda: mostrar_histograma(
      car_data,
      columna='odometer',
      titulo='Construir un histograma para la columna Odómetro'
    )
  )
  
  mostrar_checkbox_grafico(
    label='Construir gráfico de dispersión',
    accion=lambda: mostrar_dispersion(
      car_data,
      col_x='odometer',
      col_y='price',
      titulo='Construir un gráfico de dispersión para las columnas Odómetro y Precio'
    )
  )
  
if __name__ == '__main__':
  main()
