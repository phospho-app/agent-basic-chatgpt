"""
This will be the file handling the interfacing between the dev user agent repo and the app-template 
"""

from custom_agent import chat_without_memory

# This is the function that will be called when a question is asked to the agent
def ask(messages): 
    # Your code here

    # This is an example of how to get the last message received by the agent
    if len(messages) == 0:
        response = "No message received"
    else:
        response = chat_without_memory(messages)

    return response #str
