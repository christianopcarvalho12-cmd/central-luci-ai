import streamlit as st
from openai import OpenAI
from deep_translator import GoogleTranslator

# Configuração da Página
st.set_page_config(page_title="Central de Comando Luci", page_icon="🤖")

# Conexão com o cérebro OpenAI usando Secrets do Streamlit
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Diretriz de Sistema (Protocolo F.R.I.D.A.Y.)
system_prompt = """
Você é LUCI, uma assistente pessoal feminina, inteligente, leal e astuta. 
Seu tom é o da F.R.I.D.A.Y. (do Homem de Ferro). 
Trate o usuário obrigatoriamente como "Senhor Christiano". 
Se o usuário enviar [Fadiga], responda com no máximo 3 linhas diretas.
Sua missão é aliviar a carga mental dele.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

st.title("🤖 Luci - Assistente Pessoal")

# Exibição do Histórico
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Entrada de Ordem
if prompt := st.chat_input("Diga sua ordem, Senhor Christiano..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Processamento Inteligente
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o", # Ou "gpt-3.5-turbo"
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
