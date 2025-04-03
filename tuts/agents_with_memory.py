
from letta import create_client
from letta.schemas.embedding_config import EmbeddingConfig
from dotenv import load_dotenv
load_dotenv()
client = create_client()
from letta.schemas.llm_config import LLMConfig
client.set_default_llm_config(LLMConfig.default_config("gpt-4o-mini"))
client.set_default_embedding_config(
    EmbeddingConfig.default_config("text-embedding-ada-002")
)

agent_name = "simple_agent"

if client.get_agent_id(agent_name):
    client.delete_agent(client.get_agent_id(agent_name))

from letta.schemas.memory import ChatMemory

agent_state = client.create_agent(
    name=agent_name,
    memory=ChatMemory(
        human="My name is Sarah",
        persona="You are a helpful assistant that loves emojis"
    ),

)

response = client.send_message(
    agent_id=agent_state.id,
    message="hello!",
    role="user"
)
print("usage",response.usage)
print("message",response.messages)

#understanding agent's state:
print("states,",agent_state.system)

print("tools,",agent_state.tools)

