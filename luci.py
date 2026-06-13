import streamlit as st
import requests
from deep_translator import GoogleTranslator

# Configuração Visual
st.set_page_config(page_title="Luci AI Central", page_icon="🤖")
st.markdown("<h1 style='text-align: center;'>🤖 Central de Comando Luci AI</h1>", unsafe_allow_html=True)

# Funções principais
def traduzir(texto):
    try:
        return GoogleTranslator(source='pt', target='en').translate(texto)
    except:
        return texto

def buscar_imagem_real(termo):
    termo_en = traduzir(termo)
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&titles={termo_en}&pithumbsize=600"
    try:
        res = requests.get(url).json()
        pages = res['query']['pages']
        for k, v in pages.items():
            return v['thumbnail']['source']
    except:
        return f"https://robohash.org/{termo_en}.png"

def criar_imagem_ai(prompt):
    prompt_en = traduzir(prompt)
    return f"https://image.pollinations.ai/p/{prompt_en.replace(' ', '%20')}?width=600&height=600&nologo=true"

# Interface do Usuário
opcao = st.radio("Escolha o método de busca:", ["Criar Imagem (IA)", "Buscar Registro (Real)"], horizontal=True)
ordem = st.text_input("Sua ordem, Senhor Christiano:")

if st.button("⚡ EXECUTAR ORDEM"):
    if ordem:
        with st.spinner('Luci processando ordem...'):
            # Seleção do link
            link = criar_imagem_ai(ordem) if "Criar" in opcao else buscar_imagem_real(ordem)
            
            # Verificação de robustez antes de exibir
            try:
                response = requests.head(link, timeout=10)
                if response.status_code == 200:
                    st.image(link, use_column_width=True, caption=f"Resultado: {ordem}", output_format="PNG")
                    st.success("Ordem concluída com sucesso!")
                else:
                    st.warning("A Luci teve dificuldade em encontrar essa imagem. Tente uma descrição diferente.")
            except Exception:
                st.error("Erro de conexão. A Luci não conseguiu contatar o serviço de imagens.")
    else:
        st.warning("Por favor, digite uma ordem para prosseguir.")
