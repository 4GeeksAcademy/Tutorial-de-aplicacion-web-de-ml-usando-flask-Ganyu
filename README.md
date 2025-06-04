# Predicción de Tipo de Diabetes

Aplicación en Streamlit que predice el tipo de diabetes basado en parámetros clínicos y un modelo entrenado.

## Parámetros usados:
- Glucemia en ayunas
- Prueba de tolerancia a la glucosa
- Hemoglobina A1c
- BMI
- Edad
- Presión arterial sistólica

## Cómo usar en Render.com

1. Crea un nuevo Web Service.
2. Usa `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0` como comando de inicio.
3. Sube el archivo `model.pkl` junto al resto del proyecto.
