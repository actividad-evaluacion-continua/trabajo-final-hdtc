import streamlit as st
from joblib import load
import pandas as pd

# Cargar el modelo entrenado
modelo = load("./models/rf.joblib")

# Título de la app Streamlit
st.title("Predicción de Supervivencia Titanic")

# Introducción de variables a través de formularios
edad = st.number_input("Edad del pasajero:", min_value=0, max_value=100, value=28)
tarifa = st.number_input("Tarifa (Fare):", min_value=0.0, value=72.5)

# Botón para realizar la predicción
if st.button("Predecir"):
    # Hacer la predicción con el modelo cargado
    input_data = pd.DataFrame([[edad, tarifa]], columns=["Age", "Fare"])
    prediccion = modelo.predict(input_data)

    # Mostrar el resultado de la predicción
    if prediccion[0] == 1:
        st.success("¡El pasajero sobrevivió!")
    else:
        st.error("El pasajero no sobrevivió.")
