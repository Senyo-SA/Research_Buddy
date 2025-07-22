from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from pydantic import BaseModel


load_dotenv()

def research_query():

    # llm1 = ChatOpenAI(model="gpt-4o-mini")
    llm2 = ChatAnthropic(model="claude-opus-4-20250514")

    result = llm2.invoke("research")
    print(result.content)


research_query()
