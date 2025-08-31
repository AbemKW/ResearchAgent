from langchain.agents import initialize_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.llms.openai import ChatOpenAI


llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    temperature=0
)


tavily = TavilySearchResults()
tools = [tavily]


research_agent = initialize_agent(
    tools=tools,
    llm=llm
)


# Example usage
if __name__ == "__main__":
    query = input("Ask a research question: ")
    result = research_agent.run(query)
    print(result)