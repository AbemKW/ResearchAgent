from langchain.agents import initialize_agent, AgentType, Tool, load_tools
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.chat_models import ChatOpenAI

wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
tools = [wiki]
# LLM
llm = ChatOpenAI(model="qwen/qwen3-4b", base_url="http://127.0.0.1:1234/v1", api_key="lm-studio", temperature=0)

# Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# Query
while True:
    query = input("Ask a research question: ")
    if query.lower() == "exit":
        break
    response = agent.invoke(input=query)
    print("Output response:", response["output"])
    print("Full response:", response)