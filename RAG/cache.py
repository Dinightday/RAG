from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.storage import LocalFileStore
from langchain_classic.embeddings import CacheBackedEmbeddings

def embed():
    modelo_embeded = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    store = LocalFileStore("./cache/")

    cache_embeded = CacheBackedEmbeddings.from_bytes_store(
        modelo_embeded,
        store,
        namespace="cache_langchain"
    )
    return cache_embeded