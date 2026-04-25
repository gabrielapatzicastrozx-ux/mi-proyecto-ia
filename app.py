import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Detector de Emociones IA", page_icon="🧠")

st.title("🧠 Detector de Emociones con IA")
st.write("Escribe cómo te sientes o qué piensas, y la IA analizará tu sentimiento.")

texto = st.text_input("Escribe algo aquí:", placeholder="Ejemplo: Estoy muy emocionado por esta feria")

if texto:
    # La IA analiza el texto
    analisis = TextBlob(texto)
    # Traducimos polaridad a algo entendible
    polaridad = analisis.sentiment.polarity
    
    st.divider()
    st.subheader("Resultado del Análisis:")
    
    if polaridad > 0.3:
        st.balloons()
        st.success(f"🤩 ¡SUPER POSITIVO! (Puntaje: {polaridad:.2f})")
        st.write("La IA detecta mucha alegría y entusiasmo en tus palabras.")
    elif polaridad > 0:
        st.info(f"🙂 Positivo (Puntaje: {polaridad:.2f})")
        st.write("Parece que te sientes bien.")
    elif polaridad < 0:
        st.error(f"😔 Negativo (Puntaje: {polaridad:.2f})")
        st.write("La IA detecta tristeza, enojo o frustración.")
    else:
        st.warning(f"😐 Neutral (Puntaje: {polaridad:.2f})")
        st.write("No detecto una emoción clara, pareces estar tranquilo.")

st.sidebar.markdown("### ¿Cómo funciona?")
st.sidebar.write("Esta IA usa **NLP (Procesamiento de Lenguaje Natural)** para entender el valor emocional de las palabras.")
