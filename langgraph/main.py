from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator
from langgraph.graph import StateGraph, START, END


class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int

graph_builder = StateGraph(MessagesState)

def chatBot(state: MessagesState) -> MessagesState :
    #do llm call
    return {"messae": "this is a static msg retured from chat bot node"}

graph_builder.add_node("chatBot", chatBot)

