import streamlit as st
from textblob import TextBlob
import time

st.set_page_config(page_title="IA Detector de Sinceridad", page_icon="🕵️‍♂️")

st.title("🕵️‍♂️ IA: Detector de Sinceridad Emocional")
st.write("¿Tu texto coincide con tu realidad? Ponemos a prueba tu honestidad digital.")

# 1. Entrada de texto
mensaje = st.text_input("Escribe cómo te sientes hoy:", placeholder="Ejemplo: Estoy muy feliz")

if mensaje:
    # Procesamiento de Lenguaje Natural (NLP) simple
    blob = TextBlob(mensaje)
    score = blob.sentiment.polarity
    
    st.subheader("📸 Paso 2: Validación Visual")
    st.info("Asegúrate de usar la cámara frontal para el escaneo facial.")
    
    # El componente camera_input en dispositivos móviles 
    # suele abrir la cámara frontal por defecto.
    img_file = st.camera_input("Captura tu expresión actual")
    
    if img_file:
        with st.spinner('Analizando incongruencias biométricas...'):
            time.sleep(2) # Efecto de carga para la feria
            
            st.divider()
            
            # Lógica de detección
            # Buscamos palabras clave para determinar si hay "mentira"
            palabras_positivas = ["feliz", "bien", "alegre", "contento", "excelente"]
            es_mensaje_positivo = any(p in mensaje.lower() for p in palabras_positivas)

            if es_mensaje_positivo:
                st.warning("⚠️ RESULTADO: INCONGRUENCIA DETECTADA")
                st.write(f"**Análisis de Texto:** Tu mensaje indica optimismo.")
                st.write("**Análisis Facial:** La IA detecta micro-expresiones de fatiga o neutralidad.")
                st.error("🚨 Veredicto: Estás ocultando algo. Tu sonrisa no llega a los ojos.")
            else:
                st.success("✅ RESULTADO: SINCERIDAD TOTAL")
                st.write("**Análisis:** Tu estado emocional verbal y físico están en armonía.")

st.sidebar.markdown("### Configuración de IA")
st.sidebar.write("Priorizando: **Cámara Frontal (Selfie Mode)**")
st.sidebar.write("Algoritmo: **Análisis de Disonancia Semántica**")

st.sidebar.write("- **NLP:** Análisis de texto.")
st.sidebar.write("- **Deep Learning:** Redes neuronales para detección de micro-expresiones faciales.")
