# tool description
core_memory_save_description = "Save important information about you," \
+ "the agent or the human you are chatting with."

# arguments into the tool (generated by the LLM)
# defines what the agent must generate to input into the tool
core_memory_save_properties = \
{
    # arg 1: section of memory to edit
    "section": {
        "type": "string",
        "enum": ["human", "agent"],
        "description": "Must be either 'human' " \
        + "(to save information about the human) or 'agent'" \
        + "(to save information about yourself)",
    },
    # arg 2: memory to save
    "memory": {
        "type": "string",
        "description": "Memory to save in the section",
    },
}

# tool schema (passed to OpenAI)
core_memory_save_metadata = \
    {
        "type": "function",
        "function": {
            "name": "core_memory_save",
            "description": core_memory_save_description,
            "parameters": {
                "type": "object",
                "properties": core_memory_save_properties,
                "required": ["section", "memory"],
            },
        }
    }

