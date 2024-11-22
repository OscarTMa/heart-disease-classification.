import streamlit as st
import pandas as pd
import pickle
import os

# Ruta al directorio de modelos
models_dir = "models"

# Cargar los modelos
model_files = {
    'Logistic Regression': os.path.join(models_dir, "LogisticRegression.pkl"),
    'Decision Tree': os.path.join(models_dir, "DecisionTree.pkl"),
    'Random Forest': os.path.join(models_dir, "RandomForest.pkl"),
    'XGBoost': os.path.join(models_dir, "XGBoost.pkl"),
}

models = {}
for model_name, model_path in model_files.items():
    with open(model_path, "rb") as file:
        models[model_name] = pickle.load(file)

# Título de la aplicación
st.title('Heart Disease Prediction')

# Seleccionar el modelo
selected_model_name = st.selectbox('Select Model', list(models.keys()))
selected_model = models[selected_model_name]

# Crear el formulario de entrada para que el usuario ingrese los datos
age = st.slider('Age', 20, 100, 50)
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type', ['TA', 'ATA', 'NAP', 'ASY'])
trestbps = st.slider('Resting Blood Pressure', 90, 200, 120)
chol = st.slider('Cholesterol', 100, 600, 200)
fbs = st.selectbox('Fasting Blood Sugar', [0, 1])
restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST', 'LVH'])
thalach = st.slider('Maximum Heart Rate', 50, 220, 150)
exang = st.selectbox('Exercise Angina', ['Y', 'N'])
oldpeak = st.slider('Oldpeak', 0.0, 6.0, 1.0)
slope = st.selectbox('Slope of ST Segment', ['Up', 'Flat', 'Down'])

# Preprocesar los datos de entrada
input_data = pd.DataFrame({
    'Age': [age],
    'Sex': [sex],
    'ChestPainType': [cp],
    'RestingBP': [trestbps],
    'Cholesterol': [chol],
    'FastingBS': [fbs],
    'RestingECG': [restecg],
    'MaxHR': [thalach],
    'ExerciseAngina': [exang],
    'Oldpeak': [oldpeak],
    'ST_Slope': [slope]
})

# Cargar las columnas del entrenamiento
columns_path = os.path.join(models_dir, "training_columns.pkl")
with open(columns_path, "rb") as file:
    training_columns = pickle.load(file)

# Aplicar preprocesamiento
def preprocess_input(data, training_columns):
    # Codificar variables categóricas
    data = pd.get_dummies(data, columns=['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'])
    
    # Agregar columnas faltantes con valores 0
    for col in training_columns:
        if col not in data.columns:
            data[col] = 0
    
    # Reordenar las columnas para que coincidan
    data = data[training_columns]
    return data

processed_data = preprocess_input(input_data, training_columns)

# Botón para realizar la predicción
if st.button('Predict'):
    prediction = selected_model.predict(processed_data)[0]
    # Mostrar el resultado
    if prediction == 1:
        st.success(f'The patient has a higher risk of heart disease using {selected_model_name}.')
    else:
        st.success(f'The patient has a lower risk of heart disease using {selected_model_name}.')
