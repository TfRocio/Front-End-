import streamlit as st
import requests
import os
from PIL import Image

# URL de la API del backend
API_HOST = os.getenv("API_HOST")
BACKEND_URL = f"{API_HOST}/responseChatbot"


# Estilo de la página
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .title {
        color: #4a4a4a;
        text-align: center;
        padding-top: 20px;
    }
    .text-input {
        width: 70%;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 5px;
        margin: 20px auto;
    }
    .text-area {
        width: 70%;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 5px;
        margin: 20px auto;
        background-color: #fff;
    }
    .footer {
        color: #666;
        text-align: center;
        padding-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.markdown("<h1 class='title'>Chatbot de Tránsito - Ciudad de México</h1>", unsafe_allow_html=True)


# Interfaz de usuario de Streamlit
st.markdown("<h1 style='color: #FFC0CB;'>Chatbot de Tránsito</h1>", unsafe_allow_html=True)

st.write('!Hola! Soy un asistente virtual, llamado Pepe, que sabe todo sobre el Reglamento de Tránsito de la Ciudad de México. !Hazme una pregunta!')

user_input = st.text_input("Ingresa tu pregunta aquí:")
params = {
        "user_input":user_input
    }
#test
response = requests.get(BACKEND_URL, params={'user_input': user_input})
prediction = response.json()
pred = prediction['answer']
st.write(pred)


#Botón para enviar el input
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: pink;
}
</style>
""", unsafe_allow_html=True)


#if st.button("Enviar"):
    # Enviar el mensaje al backend y recibir la respuesta
 #   bot_response = send_message_to_backend(user_input)

    # Mostrar la respuesta del chatbot
  #  st.text_area("Respuesta del Chatbot:", value=bot_response, height=200, max_chars=None, key=None)

# Carga la imagen desde un archivo local
image = Image.open('ruta/a/tu/imagen.jpg')

# Muestra la imagen en tu aplicación
st.image(image, caption='Descripción opcional', use_column_width=True)


# Sección de Tips de Tránsito
st.markdown("<h2 style='color: #FFC0CB;'>Tips de Tránsito</h2>", unsafe_allow_html=True)
st.write("Aquí encontrarás consejos útiles para conducir de manera segura en la Ciudad de México:")
st.markdown("""
- Mantén una distancia segura entre vehículos en todo momento.
- Utiliza el sistema de transporte público para reducir el tráfico.
- Respeta los límites de velocidad y las señales de tránsito.
- Evita el uso del teléfono celular mientras conduces.
""")

# Sección de Preguntas Frecuentes (FAQ)
st.markdown("<h2 style='color: #FFC0CB;'>Preguntas Frecuentes (FAQ)</h2>", unsafe_allow_html=True)
st.write("Respuestas a algunas preguntas comunes sobre el reglamento de tránsito en la Ciudad de México:")
st.markdown("""
**¿Cuál es la velocidad máxima permitida en las avenidas principales?**
La velocidad máxima permitida en las avenidas principales de la Ciudad de México es de 50 km/h, a menos que se indique lo contrario.

**¿Cuál es la multa por estacionarse en un lugar prohibido?**
La multa por estacionarse en un lugar prohibido puede variar, pero generalmente es de alrededor de 700 pesos.

**¿Cuál es la sanción por manejar bajo los efectos del alcohol?**
Manejar bajo los efectos del alcohol puede resultar en una multa considerable, la suspensión de la licencia de conducir e incluso la prisión, dependiendo del grado de intoxicación y las circunstancias del incidente.
""")

# Sección de Novedades (simulada)
st.markdown("<h2 style='color: #FFC0CB;'>Novedades</h2>", unsafe_allow_html=True)
st.write("Mantente al tanto de las últimas noticias sobre tránsito en la Ciudad de México:")
st.markdown("""
- Se implementarán nuevos carriles exclusivos para bicicletas en el Centro Histórico.
- Se establecerán controles de velocidad más estrictos en las zonas escolares.
- La Ciudad de México lanzará una campaña de concientización sobre el uso del cinturón de seguridad.
""")

# Pie de página
st.markdown(
    """
    ----
    Creado por Teresita, Rodrigo y Rocío con Streamlit para Le Wagon México.
    """
)
