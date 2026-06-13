import streamlit as st

# 1. Configuração de Design Minimalista
st.set_page_config(page_title="Luci - Sistema Central", page_icon="🤖")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stChatInput { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Inicialização da Memória
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Central online, Senhor Christiano. Em que posso servir?"}]
if "data" not in st.session_state:
    st.session_state.data = {"gastos": [], "lembretes": [], "fadiga": False}

# 3. Core Inteligente (Lógica de Resposta)
def responder(prompt):
    texto = prompt.lower()
    
    if "[fadiga]" in texto:
        st.session_state.data["fadiga"] = True
        return "Protocolo de preservação ativado. Serei breve e focada apenas no essencial, Senhor."
    
    if "gasto" in texto or "gastei" in texto:
        st.session_state.data["gastos"].append(texto)
        return "Lançamento financeiro capturado com sucesso. O sistema está atualizado."
    
    if "lembrar" in texto or "agendar" in texto:
        st.session_state.data["lembretes"].append(texto)
        return "Ordem arquivada. Não deixarei escapar, Senhor Christiano."
    
    if "status" in texto:
        return f"Status: Operacional. Fadiga: {'Ativa' if st.session_state.data['fadiga'] else 'Desativada'}. Lembretes pendentes: {len(st.session_state.data['lembretes'])}."

    return "Comando recebido. Estou processando sua solicitação com a precisão necessária."

# 4. Interface
st.title("🤖 Luci - Assistente Pessoal")
st.markdown("---")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Diga sua ordem, Senhor Christiano..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    resposta = responder(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
