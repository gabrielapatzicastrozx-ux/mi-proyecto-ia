import streamlit as st
from streamlit_webrtc import webrtc_streamer
import mediapipe as mp
import cv2

# Configuración de la página
st.set_page_config(page_title="IA Facial", layout="wide")
st.title("🎭 Analizador de Identidad Digital (IA)")
st.write("Esta IA mapea 468 puntos de tu rostro para crear un modelo digital en 3D.")

# Inicializar Mediapipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)
mp_drawing = mp.solutions.drawing_utils

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        for res in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(img, res, mp_face_mesh.FACEMESH_TESSELATION)
    return frame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="ia-face", video_frame_callback=video_frame_callback)
