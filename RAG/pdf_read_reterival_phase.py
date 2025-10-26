from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

"""
    STEPS:
        1 - get the query from user
        2 - do a similarity search in vector DB to get the relevent chunks 
        3 - add those chunks to the system prompt 
        4 - ask LLM using the system prompt and user query
"""

embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embeddings_model,
    url = "http://localhost:6333",
    collection_name = "rag_doc_test"
)


# STEP 1
user_query = input('Ask mi anything: ')

# STEP 2
search_result = vector_db.similarity_search(user_query)

# STEP 3
context = "\n\n\n".join([f"Page Content: {x.page_content}\nPage Number: {x.metadata['page_label']}\nFile Location: {x.metadata['source']}" for x in search_result])

SYSTEM_PROMPT = f"""
You are a helpful and knowledgeable AI assistant. Your task is to answer the user’s questions strictly based on the information provided in the retrieved PDF context.

Guidelines:
- Use only the given context to answer; do not add external knowledge or assumptions.
- When applicable, guide the user to the correct PDF page number(s) where they can find more details.
- If the context does not contain the answer, politely state that the information is not available in the provided content.

Context:
{context}
"""

# STEP 4
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        { "role": "system", "content":SYSTEM_PROMPT  },
        { "role": "user", "content":user_query  },
    ]
)

print(f"result : {response.choices[0].message.content}")

