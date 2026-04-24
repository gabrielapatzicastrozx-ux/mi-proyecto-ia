import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
import mediapipe as mp
import numpy as np

# Configuración de Mediapipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))

st.title("🎭 IA Identity Mirror")
st.write("Acércate a la cámara para ver cómo la Inteligencia Artificial mapea tu rostro en tiempo real.")

class FaceTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Convertir a RGB para Mediapipe
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(img_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Dibujar la malla facial (Face Mesh)
                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=drawing_spec
                )
        
        return img

# Iniciar el streaming de video
webrtc_streamer(key="face-mesh", video_transformer_factory=FaceTransformer)

st.info("Esta tecnología utiliza Redes Neuronales Convolucionales para identificar 468 puntos de referencia en tu cara.")
