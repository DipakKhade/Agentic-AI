from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai"  ## figure out how to pass base url of google gen ai
)


class MessagesState(TypedDict):
    messages: list[AnyMessage]

graph_builder = StateGraph(MessagesState)

def chatBot(state: MessagesState) -> MessagesState:
    print(f"node : chatBot, state: {state}")
    #do llm call
    response = llm.invoke(state.get("messages"))
    return { "messages": [ response ] }

def dummyNode(state: MessagesState) -> MessagesState:
    print(f"node : dummyNode, state: {state}")
    return {"messages": "this is message coming from dummy node"}


# ADD THE NODES
graph_builder.add_node("chatBot", chatBot)
graph_builder.add_node("dummyNode", dummyNode)

# CONNECT THE EDGES
graph_builder.add_edge(START, "chatBot")
graph_builder.add_edge("chatBot", "dummyNode")
graph_builder.add_edge("dummyNode", END)


graph = graph_builder.compile()

updated_msg = graph.invoke({"messages":["what is 2+2"]})  ## while invoking the graph give the initial message

print(updated_msg)