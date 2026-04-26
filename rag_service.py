from langchain_qdrant import QdrantVectorStore  # Use this instead of langchain_community
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
client = QdrantClient(":memory:") # Or your local URL

# Ensure collection exists
COLLECTION_NAME = "financial_docs"
if not client.collection_exists(COLLECTION_NAME):
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

def process_and_index(text: str, metadata: dict):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )
    vector_store.add_texts(texts=chunks, metadatas=[metadata]*len(chunks))

def semantic_search(query: str, top_k: int = 5):
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )
    return vector_store.similarity_search(query, k=top_k)