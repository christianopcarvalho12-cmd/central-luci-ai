import streamlit as st
import datetime

# --- Configuração de Design ---
st.set_page_config(page_title="Luci - Central Inteligente", page_icon="🤖", layout="centered")

# --- Memória Persistente do Sistema ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Central online, Senhor Christiano. Em que posso servir?"}]
if "data" not in st.session_state:
    st.session_state.data = {"gastos": [], "lembretes": [], "fadiga": False}

# --- Core Inteligente ---
def responder(prompt):
    texto = prompt.lower()
    
    # Módulo 1: Protocolo de Fadiga (Prioridade Máxima)
    if "[fadiga]" in texto:
        st.session_state.data["fadiga"] = True
        return "Protocolo de preservação ativado. Serei breve e focada apenas no essencial, Senhor."
    
    # Módulo 2: Gestão Financeira
    if "gasto" in texto or "gastei" in texto:
        st.session_state.data["gastos"].append(texto)
        return "Lançamento financeiro capturado com sucesso. O sistema está atualizado."
    
    # Módulo 3: Agenda e Memória
    if "lembrar" in texto or "agendar" in texto:
        st.session_state.data["lembretes"].append(texto)
        return "Ordem arquivada. Não deixarei escapar, Senhor Christiano."
    
    # Módulo 4: Análise de Estado
    if "status" in texto:
        return f"Status: Operacional. Fadiga: {'Ativa' if st.session_state.data['fadiga'] else 'Desativada'}. Lembretes pendentes: {len(st.session_state.data['lembretes'])}."

    return "Comando recebido. Estou processando sua solicitação com a precisão necessária."

# --- Interface de Comando ---
st.title("🤖 Luci - Assistente Pessoal")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Diga sua ordem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    resposta = responder(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
