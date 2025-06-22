from autogen import ConversableAgent

agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": [{"model": "llama3.2", "api_key": "ollama", 
                                 "base_url": "http://localhost:11434/v1"}]},
    code_execution_config=False,  # Turn off code execution.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)
reply = agent.generate_reply(messages=[{"content": "Tell me a joke.",
                                        "role": "user"}])
print(reply)