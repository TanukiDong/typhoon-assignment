from functools import cache
from langchain_openai import ChatOpenAI

from typhoon_assignment.setting import (
    API_KEY,
    MODEL,
    BASE_URL,)

@cache
def init_llm(
    base_url=BASE_URL,
    model=MODEL,
    api_key=API_KEY,
):

    return ChatOpenAI(
        base_url=base_url,
        model=model,
        api_key=api_key
    )

if __name__ == "__main__":
    from langchain_core.messages.human import HumanMessage

    llm = init_llm()
    result = llm.invoke([HumanMessage(content="สวัสดี")])
    print(result.content)