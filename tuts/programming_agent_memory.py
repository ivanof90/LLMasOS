
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


chat_memory = ChatMemory(
    human="Name: Bob",
    persona="You are a helpful assistant"
)

print("block names,",chat_memory.list_block_labels())
print("human block,",chat_memory.get_block("human"))

#define a memory module:

from letta.schemas.memory import ChatMemory
from letta.schemas.block import Block
from typing import Optional, List
import json


class TaskMemory(ChatMemory):

    def __init__(self, human: str, persona: str, tasks: List[str]):
        super().__init__(human=human, persona=persona, limit=2000)

        self.set_block(
            block=Block(
                limit=2000,
                value=json.dumps(tasks),
                name="tasks",
                label="tasks"
            )
        )

    def task_queue_push(self: "Agent", task_description: str):
        """
        Push to a task queue stored in core memory.

        Args:
            task_description (str): A description of the next task you must accomplish.

        Returns:
            Optional[str]: None is always returned as this function
            does not produce a response.
        """
        import json
        tasks = json.loads(self.memory.get_block("tasks").value)
        tasks.append(task_description)
        self.memory.update_block_value("tasks", json.dumps(tasks))
        return None

    def task_queue_pop(self: "Agent"):
        """
        Get the next task from the task queue

        Returns:
            Optional[str]: The description of the task popped from the
            queue, if there are still tasks in queue. Otherwise, returns
            None (the task queue is empty)
        """
        import json
        tasks = json.loads(self.memory.get_block("tasks").value)
        if len(tasks) == 0:
            return None
        task = tasks[0]
        print("CURRENT TASKS: ", tasks)
        self.memory.update_block_value("tasks", json.dumps(tasks[1:]))
        return task

task_agent_name = "task_agent"

task_agent_state = client.create_agent(
    name=task_agent_name,
    system = open("task_queue_system_prompt.txt", "r").read(),
    memory=TaskMemory(
        human="My name is Sarah",
        persona="You are an agent that must clear its tasks.",
        tasks=[]
    )
)

message = "Add 'start calling me Charles'"  \
+ "and 'tell me a haiku about my name' as two seperate tasks."

response = client.send_message(
    agent_id=task_agent_state.id,
    role="user",
    message=message
)
print("messages 1:",response.messages)

response = client.send_message(
    agent_id=task_agent_state.id,
    role="user",
    message="complete your tasks"
)
print("messages 2:",response.messages)

print("block:",client.get_core_memory(task_agent_state.id).get_block("tasks"))
