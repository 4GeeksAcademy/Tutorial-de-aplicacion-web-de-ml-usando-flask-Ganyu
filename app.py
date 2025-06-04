import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargar el modelo entrenado
model = joblib.load("model.pkl")

st.set_page_config(page_title="Predicción de Diabetes", layout="wide")

st.title("🧪 Predicción de Tipo de Diabetes")
st.write("Introduce los valores clínicos del paciente:")

col1, col2 = st.columns(2)

with col1:
    glucose_fasting = st.number_input("Glucemia en ayunas (mg/dL)", 50, 400, 100)
    glucose_tolerance = st.number_input("Prueba de tolerancia a la glucosa (mg/dL)", 50, 400, 140)
    a1c = st.number_input("Hemoglobina A1c (%)", 3.0, 15.0, 5.5)
    bmi = st.number_input("Índice de Masa Corporal (BMI)", 10.0, 60.0, 25.0)

with col2:
    age = st.number_input("Edad (años)", 1, 120, 35)
    blood_pressure = st.number_input("Presión arterial sistólica (mmHg)", 80, 200, 120)

# Crear input para el modelo
input_data = pd.DataFrame({
    "glucose_fasting": [glucose_fasting],
    "glucose_tolerance": [glucose_tolerance],
    "a1c": [a1c],
    "bmi": [bmi],
    "age": [age],
    "blood_pressure": [blood_pressure]
})

if st.button("🔍 Predecir tipo de diabetes"):
    prediction = model.predict(input_data)[0]
    st.success(f"Resultado: {prediction}")

st.markdown("---")
st.subheader("📊 Tabla de referencia clínica")

reference_data = {
    "Parámetro": ["Glucemia en ayunas", "Tolerancia a la glucosa", "Hemoglobina A1c", "BMI", "Presión arterial"],
    "Valores Normales": [
        "70–99 mg/dL",
        "< 140 mg/dL a las 2h",
        "< 5.7%",
        "18.5–24.9",
        "Menor a 130 mmHg"
    ]
}

ref_df = pd.DataFrame(reference_data)
st.table(ref_df)
