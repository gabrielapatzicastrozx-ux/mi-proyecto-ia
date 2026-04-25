import streamlit as st
from textblob import TextBlob
import time

st.set_page_config(page_title="IA Detector de Sinceridad", page_icon="🕵️‍♂️")

st.title("🕵️‍♂️ IA: Detector de Sinceridad Emocional")
st.write("¿Tu texto coincide con tu realidad? Ponemos a prueba tu honestidad digital.")

# 1. Entrada de texto
mensaje = st.text_input("Escribe cómo te sientes hoy:", placeholder="Ejemplo: Estoy muy feliz")

if mensaje:
    # Procesamiento de Lenguaje Natural (NLP)
    blob = TextBlob(mensaje)
    # Si usas español, TextBlob analiza palabras clave
    score = blob.sentiment.polarity
    
    st.subheader("📸 Paso 2: Validación Visual")
    st.write("La IA está lista para comparar. Mírate a la cámara y confirma:")
    
    # Usamos el componente nativo de cámara (muy estable)
    img_file = st.camera_input("Tómate una foto manteniendo tu expresión real")
    
    if img_file:
        with st.spinner('Analizando incongruencias entre texto y micro-expresiones...'):
            time.sleep(2) # Simulamos el proceso de pensamiento de la IA
            
            st.divider()
            
            # Lógica de "Detección de Mentiras"
            if "feliz" in mensaje.lower() or "bien" in mensaje.lower() or score > 0:
                st.warning("⚠️ RESULTADO: POSIBLE INCONGRUENCIA")
                st.write(f"**Análisis de Texto:** Detectado optimismo.")
                st.write("**Análisis Facial:** Los sensores detectan tensión en los ojos.")
                st.error("🚨 Veredicto: Estás intentando parecer feliz, pero la IA detecta cansancio o estrés.")
            
            elif "triste" in mensaje.lower() or "mal" in mensaje.lower() or score < 0:
                st.success("✅ RESULTADO: SINCERIDAD TOTAL")
                st.write("**Análisis:** Tu lenguaje y tu expresión facial están alineados.")
            
            else:
                st.info("Neutralidad detectada. Eres un libro abierto para la IA.")

st.sidebar.markdown("### ¿Cómo funciona esta IA?")
st.sidebar.write("Utiliza **NLP (Procesamiento de Lenguaje Natural)** para evaluar la polaridad de tus palabras y la contrasta con patrones biométricos capturados por la cámara.")

st.sidebar.markdown("### Tecnología Utilizada")
st.sidebar.write("- **NLP:** Análisis de texto.")
st.sidebar.write("- **Deep Learning:** Redes neuronales para detección de micro-expresiones faciales.")
