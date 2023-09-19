# Load environment variables

from dotenv import load_dotenv
load_dotenv()

# import schema for chat messages and ChatOpenAI in order to query chatmodels GPT-3.5-turbo or GPT-4

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
     

chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.3)

def my_agent(input):
    messages = [
        SystemMessage(content="You are a funny and helpful assistant."),
        HumanMessage(content=input),
    ]
    
    response=chat(messages)

    return response.content
