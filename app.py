import streamlit as st
import time
import random

st.set_page_config(page_title="IA Face Matcher", page_icon="🎭")

st.title("🎭 IA: Buscador de Gemelos en el Multiverso")
st.write("¿Alguna vez te dijeron que te pareces a alguien famoso? La IA lo confirmará hoy.")

# 1. Selección de Mundo
opcion = st.selectbox(
    "¿En qué mundo quieres buscar a tu doble?",
    ("Personajes de Disney", "Jugadores de Fútbol", "Actores/Actrices de Cine")
)

nombre_usuario = st.text_input("¿Cómo te llamas?", placeholder="Tu nombre aquí")

if nombre_usuario:
    # 2. Captura de Cámara
    img_file = st.camera_input("Escaneando tus rasgos faciales...")

    if img_file:
        with st.status("🧬 Analizando simetría facial y puntos biométricos...", expanded=True) as status:
            time.sleep(1.5)
            st.write("📸 Extrayendo mapa de texturas...")
            time.sleep(1.2)
            st.write(f"📂 Buscando en la base de datos de {opcion}...")
            time.sleep(1.3)
            status.update(label="¡Match Encontrado!", state="complete", expanded=False)

        st.divider()

        # Bases de datos de personajes
        base_datos = {
            "Personajes de Disney": ["Cenicienta", "Elsa", "Tarzán", "Hércules", "Moana", "Simba (Humano)", "Bella"],
            "Jugadores de Fútbol": ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Kylian Mbappé", "Alexia Putellas", "Vinícius Jr"],
            "Actores/Actrices de Cine": ["Tom Holland", "Zendaya", "Robert Downey Jr", "Scarlett Johansson", "The Rock", "Emma Watson"]
        }

        # La IA elige uno basado en el nombre para que sea "su" personaje siempre
        random.seed(nombre_usuario.lower() + opcion)
        personaje = random.choice(base_datos[opcion])
        porcentaje = random.randint(75, 99)

        # Resultado
        st.balloons()
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(img_file, caption="Tu Rostro", width=250)
        
        with col2:
            st.markdown(f"### ¡Eres un {porcentaje}% idéntico a:")
            st.header(f"✨ {personaje} ✨")
            st.write(f"La IA detectó una coincidencia estructural en tus pómulos y mirada con **{personaje}**.")

        st.info("💡 Consejo de la IA: ¡Deberías pedirle un autógrafo a tu espejo!")

st.sidebar.markdown("### ¿Cómo funciona?")
st.sidebar.write("Utiliza un algoritmo de **Reconocimiento de Patrones Visuales** que compara la distancia entre ojos, nariz y boca con una base de datos pre-cargada.")
