from langchain_core.messages import HumanMessage, SystemMessage
from pathlib import Path
import json
import random
# import jsonlines

from typhoon_assignment.llm import init_llm
from typhoon_assignment.llm.prompt import SYSTEM_PROMPT

def gen_MCQ(
        data,
        current_dish,
        question_type,
        llm = init_llm()
        ):
    # print(current_dish["dish_name"])
    dish_name = current_dish["dish_name"]
    ingredient = random.choice(current_dish["ingredients"]).split(" ")[0]
    description = current_dish["description"]
    instruction = random.choice(current_dish["instructions"])
    questions = {
        "description" : f"Summarize {description} in one sentence and ask what dish is it describing?",
        "ingredient": f"What ingredient does the dish {dish_name} use?",
        "ingredient_amount": f"How much of {ingredient} does {dish_name} uses? Use different unit of measure for each choice.",
        # "dish": f"What dish use {ingredient} as its ingredient? Make sure the there is only 1 correct answer.",
        "tool_step": f"Summarize {instruction} in one sentence and ask what dish is it related to?"
    }

    messages = [
    SystemMessage(
        content=SYSTEM_PROMPT.format(data=data)
        ),
    HumanMessage(
        content=f"Generate a multiple choice question in json format in Thai language. Topic : {questions[question_type]}"
        )
    ]
    
    result = llm.invoke(messages).content
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
        "description",
        "ingredient",
        "ingredient_amount",
        "tool_step"
        ]
    
    for d in data:
        for t in qtypes:
            content = gen_MCQ(data, d, t)
            print(content)
            q.append(content)

    save_data(q)