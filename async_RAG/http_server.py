from fastapi import FastAPI, Request
from async_RAG.redis.client import chat_queue
from async_RAG.worker.worker import chat_worker

app = FastAPI()

@app.post('/chat')
async def chat(request: Request):
    user_query = (await request.json()).get('content')

    job = chat_queue.enqueue(chat_worker, user_query)

    return {"status" : "queued", "job_id" : job.id}


@app.get('/chat_result')
async def chat_result(req: Request):
    job_id = req.query_params.get('job_id')
    print("-"*30)
    print(job_id)
    print("-"*30)

    job = chat_queue.fetch_job(job_id=job_id)
    print("-"*30)
    print(job)
    print("-"*30)

    result = job.return_value()

    return {
        "result" : result
    }
