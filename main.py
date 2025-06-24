from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

# llm1 = ChatOpenAI(model="gpt-4o-mini")
llm2 = ChatAnthropic(model="claude-opus-4-20250514")

result = llm2.invoke("10 random computer science facts")
print(result)
