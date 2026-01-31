from cache import embed
from documents import documento
from langchain_community.vectorstores import Chroma

document = documento()
embed = embed()

chromadb = Chroma.from_documents(documents=document, embedding=embed, persist_directory="./cache_embedding/")

def search_chroma(valor):

    meu_filtro = {"Data": valor} if valor is not None else None

    response_chroma = chromadb.as_retriever(search_kwargs={"k": 1, "filter": meu_filtro})
    return response_chroma