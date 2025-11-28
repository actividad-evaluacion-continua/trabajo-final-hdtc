# Importamos la función load de joblib para cargar
# modelos previamente guardados
from joblib import load

# Cargamos el modelo de Random Forest que ya
# entrenamos y guardamos en un archivo .joblib
rf_loaded = load("./models/rf.joblib")

# Realizamos una predicción para un nuevo ejemplo
# La lista [[28, 72.5]] representa las características
# del nuevo pasajero:
# - 28 años de edad
# - Fare (tarifa) de 72.5
prediction = rf_loaded.predict([[28, 72.5]])

# Mostramos la predicción en consola
# prediction[0] extrae el valor del array devuelto por predict
# 0 significa que el modelo predice que no sobrevivió
# 1 significaría que sobrevivió
print("Predicción:", prediction[0])
