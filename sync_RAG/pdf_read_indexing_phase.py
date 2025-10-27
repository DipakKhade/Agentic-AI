from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

"""
    STEPS: 
        1 - Read the File
        2 - create the chunks
        3 - create embeddings from chunks
        4 - store them in vector DB
"""

# STEP 1
loader = PyPDFLoader(file_path="/Users/dipakkhade/projects/Agentic-AI/RAG/THE_RUST.pdf")

docs = loader.load()

# STEP 2
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=400     #since we dont want to loose the context, we have to take some chunks from the previous chunk created
)

chunks = text_splitter.split_documents(documents=docs)

# STEP 3

embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"    ##google api is not working here 
)

# STEP 4

vector_db = QdrantVectorStore.from_documents(
    documents= chunks,
    embedding=embeddings_model,
    url = "http://localhost:6333",
    collection_name = "rag_doc_test"
)