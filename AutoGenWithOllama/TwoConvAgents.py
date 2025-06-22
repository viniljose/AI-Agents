from autogen import ConversableAgent

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config={"config_list": [{"model": "llama3.2", "api_key": "ollama", 
                                 "base_url": "http://localhost:11434/v1"}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={"config_list": [{"model": "llama3.2", "api_key": "ollama", 
                                 "base_url": "http://localhost:11434/v1"}]},
    human_input_mode="NEVER",  # Never ask for human input.
)
result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=2)