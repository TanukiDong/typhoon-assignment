from pathlib import Path
import json

def load_data(n):
    DIR = Path(__file__).parent / f"data/mcq{n}.jsonl"

    with open(DIR, "r") as file:
        content = [json.loads(line) for line in file]

    return content


if __name__ == "__main__":
    score = 0
    chat_ans = ["a","e","a","a","e","b","c","b","c","b","b","a","b","b","b","c","c","b","a","b","b","a","a","b","b","c","a","b","d","a","c","a","c","b","c","c"]
    chat_ans = ["a","b","b","a","b","a","a","b","c","b","a","a","c","b","c","b","b","b","b","c","c","b","b","b","b","c","b","b","b","a","b","b","c","b","b","c"]
    answer = []
    data = load_data(2)
    for content in data:
        answer.append(content["answer"])
    # print(answer)
    # print(chat_ans)
    for i in range(len(answer)):
        if answer[i] == chat_ans[i]:
            score += 1
    print(f"Chat performed {score}/{len(answer)}")
