from documents import documento
import streamlit as st
from chroma import search_chroma
from chatbot import chat
from time import time

docs = documento()

def web():
        st.set_page_config(layout="wide", page_title="RAG")

        if 'lista_memoria' not in st.session_state:
                st.session_state.lista_memoria = None

        st.title("Primeiro App RAG")

        data_salva = []

        for data in range(len(docs)):
                doc_data = docs[data].metadata['Data']
                data_salva.append(doc_data)

        busca = st.text_input(label="Filtro:", label_visibility="visible", width=100)

        botao_filtro = st.button("Filtrar", use_container_width=True)
        botao_sem_filtro = st.button("Sem filtro", use_container_width=True)

        if botao_filtro:
                if busca in data_salva:
                        st.success("Filtro aplicado")

                        st.session_state.lista_memoria = busca
                        
                        search_chroma(valor=st.session_state.lista_memoria)

        if botao_sem_filtro:
                st.success("Sem filtro aplicado.")

                search_chroma(valor=None)

        prompt_ia = st.text_area(label="Pergunta para a IA", max_chars=256)

        botao_prompt = st.button("Enviar")

        if botao_prompt:
                time_a = time()
                with st.spinner("Gerando resposta da IA."):
                        st.success("Resposta gerada!")

                        resposta_ia = chat(prompt_ia, filtro=st.session_state.lista_memoria)
                        st.write(resposta_ia)
                time_b = time()
                st.info(f"Tempo de resposta: {time_b - time_a}:.2f")