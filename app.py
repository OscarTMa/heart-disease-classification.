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
cp = st.selectbox('Chest Pain Type', [1, 2, 3, 4])  # Ejemplo de valores de CP
trestbps = st.slider('Resting Blood Pressure', 90, 200, 120)
chol = st.slider('Cholesterol', 100, 600, 200)
fbs = st.selectbox('Fasting Blood Sugar', [0, 1])
restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
thalach = st.slider('Maximum Heart Rate', 50, 220, 150)
exang = st.selectbox('Exercise Angina', [0, 1])
oldpeak = st.slider('Oldpeak', 0.0, 6.0, 1.0)
slope = st.selectbox('Slope of ST Segment', [1, 2, 3])

# Preprocesar los datos de entrada
sex = 1 if sex == 'Male' else 0

# Crear el DataFrame para la predicción
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

# Botón para realizar la predicción
if st.button('Predict'):
    prediction = selected_model.predict(input_data)[0]
    # Mostrar el resultado
    if prediction == 1:
        st.success(f'The patient has a higher risk of heart disease using {selected_model_name}.')
    else:
        st.success(f'The patient has a lower risk of heart disease using {selected_model_name}.')
