import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Luci - Sistema Central", page_icon="🤖")

# Estilização Refinada (CSS)
st.markdown("""
    <style>
    /* Fundo escuro padrão */
    .stApp {
        background-color: #0d1117;
    }
    
    /* Título com brilho */
    h1 {
        color: #00f2ff !important;
        text-shadow: 0 0 15px #00f2ff;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Bolhas de Chat: Removendo o fundo padrão e criando o estilo bordado */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        border: 1px solid #004d4d !important;
        border-radius: 10px;
        padding: 10px;
    }
    
    /* Ícones e cores baseados na sua imagem */
    [data-testid="stChatMessageAvatar"] {
        background-color: transparent !important;
    }
    
    /* Input do Chat */
    [data-testid="stChatInput"] {
        background-color: #1a1f26 !important;
        border: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

# Lógica (Mantida igual)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Central online, Senhor Christiano. Em que posso servir?"}]

st.title("🤖 Luci - Sistema Central")

for msg in st.session_state.messages:
    # Ajuste para identificar quem fala e colocar o emoji correto
    with st.chat_message(msg["role"], avatar="🤖" if msg["role"] == "assistant" else "👤"):
        st.write(msg["content"])

if prompt := st.chat_input("Diga sua ordem, Senhor Christiano..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun() # Atualiza para mostrar a mensagem imediatamente
