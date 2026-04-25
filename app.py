import streamlit as st
import time

st.set_page_config(page_title="IA Bio-Shield", page_icon="🔐", layout="centered")

# Estilo visual impactante
st.title("🔐 IA Bio-Shield: Access Control")
st.markdown("---")

st.subheader("Paso 1: Identificación por Voz/Texto")
user_id = st.text_input("Ingrese su frase de seguridad (Passphrase):", placeholder="Ejemplo: El cielo está despejado hoy")

if user_id:
    st.info("🔄 Procesando frecuencia semántica...")
    time.sleep(1)
    
    st.subheader("Paso 2: Escaneo de Biometría Facial")
    st.write("Colóquese frente al sensor (Cámara Frontal)")
    
    # Cámara frontal
    img_file = st.camera_input("Iniciando escaneo de retina y puntos faciales...")

    if img_file:
        progress_bar = st.progress(0)
        status_text = st.empty()

        # Simulacro de análisis profundo
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
            if i < 30: status_text.text("🔍 Detectando puntos de referencia...")
            elif i < 60: status_text.text("🧬 Analizando patrón de iris...")
            else: status_text.text("🛰️ Verificando base de datos global...")

        st.divider()

        # Lógica de "Acceso" basada en la longitud del texto o palabras clave
        if len(user_id) > 15:
            st.success("✅ IDENTIDAD VERIFICADA")
            st.balloons()
            st.write("### 📂 ACCESO CONCEDIDO")
            st.write("**Usuario:** Agente Especial - Feria de IA")
            st.write("**Nivel de Confianza:** 98.7%")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW9ueW9ueW9ueW9ueW9ueW9ueW9ueW9ueW9ueW9ueW9ueSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjPQCK9Lp3pG8/giphy.gif", width=300)
        else:
            st.error("❌ ACCESO DENEGADO")
            st.write("**Motivo:** El patrón de voz/texto no coincide con los rasgos faciales detectados.")
            st.write("Intente con una frase más larga para sincronizar la biometría.")
            st.warning("⚠️ Alerta de seguridad enviada al servidor central.")

st.sidebar.markdown("### Especificaciones Técnicas")
st.sidebar.write("• **Motor:** Neural Pattern Matcher v4.2")
st.sidebar.write("• **Seguridad:** Encriptación de grado militar")
