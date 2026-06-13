import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Luci - Sistema Central", page_icon="🤖", layout="centered")

# 2. CSS Customizado para integrar a imagem como interface
st.markdown("""
    <style>
    /* Aplica a imagem como fundo do app */
    .stApp {
        background: url('https://i.imgur.com/SeuLinkAqui.jpg') no-repeat center center fixed;
        background-size: cover;
        background-color: #050a0f;
    }

    /* Remove fundo branco padrão das mensagens e deixa transparente */
    [data-testid="stChatMessage"] {
        background-color: rgba(0, 25, 40, 0.6) !important;
        border: 1px solid #00f2ff !important;
        border-radius: 10px;
        color: #e0f7fa !important;
    }

    /* Estilização do Título */
    h1 {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff;
        text-align: center;
    }

    /* Input do Chat */
    [data-testid="stChatInput"] {
        background-color: rgba(0, 20, 30, 0.8) !important;
        border: 1px solid #00f2ff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Lógica do Sistema
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Central online, Senhor Christiano. Em que posso servir?"}]

st.title("🤖 Luci - Sistema Central")

# Exibição do Chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Processamento
if prompt := st.chat_input("Diga sua ordem, Senhor Christiano..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
    resposta = "Comando recebido. Estou processando sua solicitação com a precisão necessária."
    
    with st.chat_message("assistant"):
        st.write(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
