from redis import Redis
from rq import Queue

redis_conn = Redis()

chat_queue = Queue('chat_queue', connection=redis_conn)
