import os

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from parea import Parea
from parea.utils.trace_integrations.langchain import PareaAILangchainTracer

load_dotenv()

p = Parea(api_key=os.getenv("PAREA_API_KEY"))
handler = PareaAILangchainTracer(p)

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
prompt = ChatPromptTemplate.from_messages([("user", "{input}")])
chain = prompt | llm | StrOutputParser()


def main():
    return chain.invoke(
        {"input": "Write a Hello World program in Python using FastAPI."},
        config={"callbacks": [handler]},
    )


if __name__ == "__main__":
    print(main())
