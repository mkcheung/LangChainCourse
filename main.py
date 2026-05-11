from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from tavily import TavilyClient

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer:str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")


tavily = TavilyClient()

# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for 
#     Returns:
#         The search results
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)


# llm = ChatOpenAI(model='gpt-5')
llm = ChatOllama(model="llama3.2")
# tools = [search]
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)
def main():
    print('Hello from langchain-course!')
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")})
    print(result["messages"][-1].content)

if __name__ == '__main__':
    main()