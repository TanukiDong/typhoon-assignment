from langchain_core.messages import HumanMessage, SystemMessage
from pathlib import Path
import json
# import jsonlines

from typhoon_assignment.llm.llm import init_llm
from typhoon_assignment.llm.prompt import SYSTEM_PROMPT

def gen_MCQ(
        data,
        current_dish,
        question_type,
        llm = init_llm()
        ):
    # print(current_dish["dish_name"])
    dish_name = current_dish["dish_name"]
    questions = {
        "ingredient": f"What ingredient does the dish {dish_name} use?",
        "ingredient_amount": f"How much of an ingredient does the {dish_name} uses?",
        "dish": f"Given an ingredient, what dish use this ingredient?",
        "tool": f"What tool is required to make a {dish_name}?",
        "tool_step": f"Select a random cooking step from {dish_name}'s instruction. What tool is used in this step?"
    }

    messages = [
    SystemMessage(
        content=SYSTEM_PROMPT.format(data=data)
        ),
    HumanMessage(
        content=f"Give me a multiple choice question about : {questions[question_type]}"
        )
    ]
    
    result = llm.invoke(messages)
    return result


def load_data():
    DIR = Path(__file__).parent / "data/recipe.json"

    with open(DIR, "r") as file:
        content = json.load(file)

    return content

def save_data(data):
    DIR = Path(__file__).parent / "data/mcq.jsonl"

    with open(DIR, "w", encoding="utf-8") as file:
        for entry in data:
            # print(entry)
            # json.dump(entry, file, ensure_ascii=False)
            file.write(entry)
            file.write("\n")
    return

if __name__ == "__main__":
    data = load_data()

    q = []
    qtypes = [
        "ingredient",
        "ingredient_amount",
        "dish",
        "tool",
        "tool_step"
        ]
    
    for d in data:
        for t in qtypes:
            content = gen_MCQ(data, d, t)
            print(content.content)
            q.append(content.content)

    # save_data(q)