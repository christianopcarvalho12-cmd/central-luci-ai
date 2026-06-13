import streamlit as st

# Configuração Oficial de Design
st.set_page_config(
    page_title="Luci - Sistema Central", 
    page_icon="🤖", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

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
st.title("🤖 Luci - Assistente Pessoal")
st.subheader("Sistema de Gerenciamento de Vida")

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
