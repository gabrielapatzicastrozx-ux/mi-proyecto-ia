import streamlit as st
from deepface import DeepFace
from streamlit_webrtc import webrtc_streamer
import cv2
import numpy as np

st.set_page_config(page_title="IA Detector de Sinceridad", page_icon="🕵️‍♂️")

st.title("🕵️‍♂️ IA: ¿Dices la verdad sobre cómo te sientes?")
st.write("Escribe tu estado de ánimo y luego deja que la IA analice tu rostro.")

# 1. Entrada de Texto
mensaje = st.text_input("Escribe cómo te sientes hoy:", placeholder="Ejemplo: Estoy muy feliz")

# 2. Entrada de Cámara
img_file = st.camera_input("Ahora tómate una foto para verificar tu emoción")

if img_file and mensaje:
    # Convertir la imagen para que la IA la entienda
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)
    
    try:
        # Analizar la cara con DeepFace
        analisis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emocion_cara = analisis[0]['dominant_emotion']
        porcentaje = analisis[0]['emotion'][emocion_cara]

        st.subheader("--- Resultado del Análisis ---")
        
        # Lógica de comparación "Sinceridad"
        if "feliz" in mensaje.lower() or "bien" in mensaje.lower():
            if emocion_cara == 'happy':
                st.success(f"✅ ¡SINCERO! Tu cara confirma tu alegría ({porcentaje:.1f}%)")
            else:
                st.error(f"⚠️ ¡DETECTADO! Dices estar feliz, pero tu cara refleja: {emocion_cara}")
                st.write("Frase recomendada: 'Parece que estás intentando poner buena cara, pero la IA nota algo diferente'.")
        
        elif "triste" in mensaje.lower() or "mal" in mensaje.lower():
            if emocion_cara in ['sad', 'neutral']:
                st.info(f"🤝 Coherente. Tu rostro coincide con tu sentimiento de {emocion_cara}.")
            else:
                st.warning(f"🤔 Curioso. Dices estar mal, pero detecto una emoción de {emocion_cara}.")

    except Exception as e:
        st.error("La IA no pudo ver bien tu rostro. ¡Intenta con más luz!")

st.sidebar.markdown("### Tecnología Utilizada")
st.sidebar.write("- **NLP:** Análisis de texto.")
st.sidebar.write("- **Deep Learning:** Redes neuronales para detección de micro-expresiones faciales.")
