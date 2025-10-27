from fastapi import FastAPI, Request
from async_RAG.redis.client import chat_queue
from async_RAG.worker.worker import chat_worker

app = FastAPI()

@app.post('/chat')
async def chat(request: Request):
    user_query = (await request.json()).get('content')

    job = chat_queue.enqueue(chat_worker, user_query)

    return {"job_id" : job.id}


    