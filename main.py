from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for 
    Returns:
        The search results
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"

# llm = ChatOpenAI(model='gpt-5')
llm = ChatOllama(model="llama3.2")
tools = [search]
agent = create_agent(model=llm, tools=tools)
def main():
    print('Hello from langchain-course!')
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})
    for message in result["messages"]:
        message.pretty_print()

if __name__ == '__main__':
    main()