import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from deep_translator import GoogleTranslator

# Configuração da Página
st.set_page_config(page_title="Central Luci AI", page_icon="🤖")

st.title("🤖 Central de Comando Luci AI")
st.subheader("Sistema Integrado de Inteligência")

# Funções do Cérebro da Luci
def buscar_imagem(termo):
    # Logica de busca (mantendo a que desenvolvemos)
    url = f"https://image.pollinations.ai/p/{termo}?width=600&height=600&nologo=true"
    return url

# Interface do Usuário
comando = st.text_input("Digite sua ordem (Ex: Crie a imagem de um gato espacial):")

if st.button("EXECUTAR ORDEM"):
    if comando:
        with st.spinner('Luci processando...'):
            url_img = buscar_imagem(comando)
            st.image(url_img, caption=f"Resultado para: {comando}")
    else:
        st.warning("Por favor, digite um comando.")