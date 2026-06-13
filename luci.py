import streamlit as st
import openai # Preparado para o cérebro principal
from deep_translator import GoogleTranslator

# Configuração da Página
st.set_page_config(page_title="Central de Comando Luci", page_icon="🤖")
st.title("🤖 Luci - Assistente Pessoal")

# Personalidade F.R.I.D.A.Y. (Diretriz do Protocolo)
system_prompt = """
Você é LUCI, uma assistente pessoal feminina, inteligente, leal e astuta. 
Seu tom é o da F.R.I.D.A.Y. (do Homem de Ferro). 
Trate o usuário estritamente como "Senhor Christiano". 
Se o usuário enviar [Fadiga], responda com no máximo 3 linhas diretas.
Sua missão é eliminar burocracias e reduzir a carga mental dele.
"""

# Inicialização do Histórico de Conversa
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# Exibição do Histórico
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Entrada de Dados
if prompt := st.chat_input("Diga sua ordem, Senhor Christiano..."):
    # Exibe mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Lógica de Resposta (SIMULAÇÃO DE AGENTE)
    with st.chat_message("assistant"):
        # Aqui a Luci processa o comando (ex: interpreta [Fadiga] ou /agenda)
        if "[Fadiga]" in prompt:
            resposta = "Entendido, Senhor. Reduzindo carga cognitiva. O que é urgente?"
        else:
            resposta = f"Às ordens, Senhor Christiano. Processando: '{prompt}'."
        
        st.markdown(resposta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})

# Módulos de Expansão (Sidebar)
with st.sidebar:
    st.header("Módulos Ativos")
    st.write("✅ Cérebro Externo")
    st.write("⏳ Módulo de Fadiga")
    if st.button("Limpar Memória"):
        st.session_state.messages = [{"role": "system", "content": system_prompt}]
        st.rerun()
