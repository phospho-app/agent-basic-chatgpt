"""
This will be the file handling the interfacing between the dev user agent repo and the app-template 
"""

### YOUR CUSTOM STARTS HERE ###

from dotenv import load_dotenv

from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

# Laod the environment variables from the .env file
load_dotenv()

# Define the prompt template tha will be used to create the context of a new chats
# In this exemple, we want the LLM to know that it is a phospho agent and that it should state its name every time it speaks
template = """Your name is phospho agent. Every time you speak, you state your name.
{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "human_input"], 
    template=template
)

# Let's create the LLMChain object that will be used to chat. Please not that the memory is not used here.
# To implement the memory, you can use the whole messages object
chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=prompt, 
    verbose=False, 
    memory=ConversationBufferWindowMemory(k=2),
)

def chat_without_memory(messages): # Takes as argument the template.py messages object (the argument of the ask() function)
    # Your code here
    last_message = messages[-1]["content"]
    output = chatgpt_chain.predict(human_input=last_message)

    return output #str

### YOUR CUSTOM ENDS HERE ###

### INTERFACE ###

# This is the function that will be called when a question is asked to the agent
def ask(messages): 
    # Your code here

    # This is an example of how to get the last message received by the agent
    if len(messages) == 0:
        response = "No message received"
    else:
        response = chat_without_memory(messages)

    return response #str
