import streamlit as st

# Configuração Oficial de Design
st.set_page_config(
    page_title="Luci - Sistema Central", 
    page_icon="🤖", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização da Interface (CSS)
st.markdown("""
    <style>
    /* Aplica a interface visual como background */
    .stApp {
        background: url('app/static/luci_interface.png') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* Faz o chat parecer parte da interface de vidro (Glassmorphism) */
    [data-testid="stChatMessage"] {
        background-color: rgba(0, 15, 25, 0.7) !important;
        border: 1px solid rgba(0, 242, 255, 0.3);
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    /* Ajustes de texto */
    h1, h2 {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff;
        text-align: center;
    }
    
    /* Input do chat estilizado */
    [data-testid="stChatInput"] {
        background-color: rgba(0, 20, 30, 0.8) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Inicialização da Memória
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Central online, Senhor Christiano. Em que posso servir?"}]
if "data" not in st.session_state:
    st.session_state.data = {"gastos": [], "lembretes": [], "fadiga": False}

# Lógica
def responder(prompt):
    texto = prompt.lower()
    if "[fadiga]" in texto:
        st.session_state.data["fadiga"] = True
        return "Protocolo de preservação ativado. Serei breve."
    if "status" in texto:
        return f"Status: Operacional. Fadiga: {'Ativa' if st.session_state.data['fadiga'] else 'Desativada'}."
    return "Comando recebido. Estou processando sua solicitação com a precisão necessária."

# Interface Nativa
st.title("🤖 Luci - Sistema Central")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Diga sua ordem, Senhor Christiano..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
    resposta = responder(prompt)
    
    with st.chat_message("assistant"):
        st.write(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
