from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from pydantic import BaseModel


load_dotenv()

# llm1 = ChatOpenAI(model="gpt-4o-mini")
llm2 = ChatAnthropic(model="claude-opus-4-20250514")

result = llm2.invoke("random computing fact")
print(result.content)
