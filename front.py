import streamlit as st
from app import process_video

# Configuração inicial
st.title("TikTok Clip Generator")
st.subheader("Transforme vídeos do YouTube em clipes virais para TikTok 🎥")

# Entrada do link do vídeo
video_url = st.text_input("Cole o link do vídeo do YouTube aqui:")

# Botão de ação
if st.button("Gerar clipes"):
    if video_url:
        st.write("🔄 Processando o vídeo...")
        result = process_video(video_url)

    else:
        st.warning("⚠️ Por favor, insira um link válido do YouTube.")
