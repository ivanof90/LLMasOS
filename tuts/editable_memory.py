from dotenv import load_dotenv
from openai import OpenAI
import os
from editable_memory_tool import *

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

model = "gpt-4o-mini"

system_prompt = "You are a chatbot." #just a simple prompt

# Make the completion request with the tool usage
chat_completion = client.chat.completions.create(
    model=model,
    messages=[
        # system prompt: always included in the context window
        {"role": "system", "content": system_prompt},
        # chat history (evolves over time)
        {"role": "user", "content": "What is my name?"},
    ]
)
print(chat_completion.choices[0].message.content) #it doesnt know my name... yet

##Adding memory to the context...

agent_memory = {"human": "Name: Bob"}
system_prompt = "You are a chatbot. " \
+ "You have a section of your context called [MEMORY] " \
+ "that contains information relevant to your conversation"

import json


chat_completion = client.chat.completions.create(
    model=model,
    messages=[
        # system prompt
        {"role": "system", "content": system_prompt + "[MEMORY]\n" + \
         json.dumps(agent_memory)},
        # chat history
        {"role": "user", "content": "What is my name?"},
    ],
)
print(chat_completion.choices[0].message.content) # now it knows my name

# Memory tool
agent_memory = {"human": "", "agent": ""}

def core_memory_save(section: str, memory: str):
    agent_memory[section] += '\n'
    agent_memory[section] += memory
print(agent_memory)

core_memory_save("human", "The human's name is Charles")

print(agent_memory)
print(core_memory_save_metadata)

agent_memory = {"human": ""}
system_prompt = "You are a chatbot. " \
+ "You have a section of your context called [MEMORY] " \
+ "that contains information relevant to your conversation"

chat_completion = client.chat.completions.create(
    model=model,
    messages=[
        # system prompt
        {"role": "system", "content": system_prompt},
        # memory
        {"role": "system", "content": "[MEMORY]\n" + json.dumps(agent_memory)},
        # chat history
        {"role": "user", "content": "My name is Bob"},
    ],
    # tool schemas
    tools=[core_memory_save_metadata]
)
response = chat_completion.choices[0]
print(response)
# openai doesnt call the tool automatically (not like langchain)
arguments = json.loads(response.message.tool_calls[0].function.arguments)
print("arguments",arguments)
core_memory_save(**arguments)
print(agent_memory)