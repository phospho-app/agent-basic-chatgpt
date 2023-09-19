from phospho import Agent, Message

# My scripts
from myagent import my_agent

agent = Agent()

@agent.chat()
def my_chat(message):
    response = my_agent(message.content)

    return Message(response)
