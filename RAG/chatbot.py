import os
from dotenv import load_dotenv
from chroma import search_chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from template import prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

os.environ["GOOGLE_API_KEY"]

prompt_file = prompt()

config_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

def chat(pergunta, filtro=None):
    retriever = search_chroma(filtro)

    chain = {"documento": retriever, "question": RunnablePassthrough()} | prompt_file |config_llm | StrOutputParser()

    response = chain.invoke(pergunta)
    return response