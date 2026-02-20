import streamlit as st

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
if edad > 50 :
    st.write("YA ESRES VIEJO")
