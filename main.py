from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
load_dotenv()

def main():
    # print("Hello from langchain-course!")

    summary_template = """ given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm

    information = "Elon Musk is a billionaire entrepreneur known for Tesla and SpaceX."
    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
