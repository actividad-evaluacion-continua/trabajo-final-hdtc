import streamlit as st
from joblib import load
import pandas as pd
import altair as alt

# --- Cargar modelo ---
modelo = load("./models/rf.joblib")

# --- Título de la app ---
st.title("Predicción de Supervivencia Titanic")

# --- Introducción de variables ---
edad = st.number_input("Edad del pasajero:", min_value=0, max_value=100, value=28)
tarifa = st.number_input("Tarifa (Fare):", min_value=0.0, value=72.5)

# --- Predicción ---
if st.button("Predecir"):
    input_data = pd.DataFrame([[edad, tarifa]], columns=["Age", "Fare"])
    prediccion = modelo.predict(input_data)
    if prediccion[0] == 1:
        st.success("¡El pasajero sobrevivió!")
    else:
        st.error("El pasajero no sobrevivió.")

# --- Sección de métricas históricas ---
st.header("Métricas históricas del modelo")

# Datos simulados
metricas = pd.DataFrame(
    {
        "Métrica": ["Precisión", "Recall", "F1-score", "Exactitud"],
        "Valor": [0.82, 0.78, 0.80, 0.81],
    }
)

# Crear gráfico de barras con Altair
grafico = (
    alt.Chart(metricas)
    .mark_bar()
    .encode(x="Métrica", y="Valor", color="Métrica")
    .properties(width=600, height=400)
)

# Mostrar gráfico en Streamlit
st.altair_chart(grafico)
