from autogen import ConversableAgent, UserProxyAgent

# Create the agent that uses the LLM.
assistant = ConversableAgent("agent",  llm_config={"config_list": [{
    "model": "llama3.2", "api_key": "ollama", 
    "base_url": "http://localhost:11434/v1"}]})

# Create the agent that represents the user in the conversation.
user_proxy = UserProxyAgent(
    "user",
    code_execution_config={
        "work_dir": "working",
        "use_docker": False,
    },
    human_input_mode="ALWAYS",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
)

# Start the conversation.
user_proxy.initiate_chat(assistant, message="write a snake game using Pygame?")
