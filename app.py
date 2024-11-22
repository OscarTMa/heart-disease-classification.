import streamlit as st
import pandas as pd
import numpy as np

###############################
# Entrenar y guardar cada modelo
for model_name, model in models.items():
    model.fit(X_train, y_train)
    model_path = os.path.join(models_dir, f"{model_name}.pkl")
    with open(model_path, "wb") as file:
        pickle.dump(model, file)
    print(f"Model {model_name} saved at {model_path}")
###############################
# Crear el formulario de entrada para que el usuario ingrese los datos
st.title('Heart Disease Prediction')

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
restecg = int(restecg)
exang = int(exang)

# Crear el DataFrame para hacer la predicción
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

# Realizar la predicción
prediction = model.predict(input_data)

# Mostrar el resultado
if prediction == 1:
    st.success('The patient has a higher risk of heart disease.')
else:
    st.success('The patient has a lower risk of heart disease.')
