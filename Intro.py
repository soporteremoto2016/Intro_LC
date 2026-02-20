import streamlit as st
from PIL import Image

st.title("Mi Primera pagina Iteractiva")
# Texto
st.write("Esta es una interfaz muy sencilla.")
# Entrada de texto
nombre = st.text_input("Escribe tu nombre:")
# Botón
if st.button("Saludar"):
    st.success(f"Hola {nombre}, bienvenido a Streamlit 🚀")
# Slider
edad = st.slider("Selecciona tu edad:", 0, 100, 25)
st.write("Tu edad es:", edad)
if edad >= 50 and edad < 80:
    st.write("ESTAS EN LA MEJOR EDAD")
    image = Image.open('JJF.jpg')
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption="Imagen exclusiva")

elif edad <= 49 :
    st.write("SIGUE ADELANTE AUN ERES MUY JOVEN")
    image1 = Image1.open('JF.jpg')
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image(image1, caption="Imagen exclusiva")

else : 
    st.write("YA ERES UN GEBEN EN LA EDAD DORADA")
    image2 = Image2.open('JAF.jpg')
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image(image2, caption="Imagen exclusiva")

