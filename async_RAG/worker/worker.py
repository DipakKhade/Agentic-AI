
async def chat_worker(input: str):
    """
    STEPS:
        1 - get the query from user
        2 - do a similarity search in vector DB to get the relevent chunks 
        3 - add those chunks to the system prompt 
        4 - ask LLM using the system prompt and user query
    """ 
    result = ''
    return result