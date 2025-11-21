import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from joblib import dump

# ================================
# 1. CARGA DEL DATASET
# ================================
# Importamos el dataset Titanic desde la carpeta local.
df = pd.read_csv("./datasets/Titanic-Dataset.csv")

# ================================
# 2. LIMPIEZA Y PREPROCESADO DE DATOS
# ================================

# Eliminamos columnas que no aportan información útil al modelo
df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1, inplace=True)

# Rellenamos valores faltantes:
# Usamos la mediana para edades
df["Age"].fillna(df["Age"].median(), inplace=True)
# Usamos la mediana para tarifas
df["Fare"].fillna(df["Fare"].median(), inplace=True)
df["Embarked"].fillna(
    df["Embarked"].mode()[0], inplace=True
)  # Usamos la moda para embarque

# Convertimos la variable categórica 'Sex' a numérica
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# Transformamos 'Embarked' a variables dummy (one-hot encoding)
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

# ================================
# 3. SELECCIÓN DE FEATURES Y TARGET
# ================================

# Usamos solo dos características simples para
# predicción: Age y Fare
X = df[["Age", "Fare"]]

# Variable objetivo: si sobrevivió o no
y = df["Survived"]

# ================================
# 4. DIVISIÓN EN TRAIN Y TEST
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# ================================
# 5. ESCALADO DE VARIABLES
# ================================
# Aunque Random Forest no lo necesita, escalar
# puede mejorar estabilidad numérica
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ================================
# 6. ENTRENAMIENTO DEL MODELO: RANDOM FOREST
# ================================
rf = RandomForestClassifier(
    n_estimators=200,  # Número de árboles
    max_depth=None,  # Sin límite de profundidad
    random_state=42,  # Reproducibilidad
)

rf.fit(X_train_scaled, y_train)  # Entrenamiento
y_pred = rf.predict(X_test_scaled)  # Predicción

# ================================
# 7. EVALUACIÓN DEL MODELO
# ================================

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

dump(rf, "./models/rf.joblib")
