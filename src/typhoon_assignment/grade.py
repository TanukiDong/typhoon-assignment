from pathlib import Path
import json

def load_data(n):
    DIR = Path(__file__).parent / f"data/mcq{n}.jsonl"

    with open(DIR, "r") as file:
        content = [json.loads(line) for line in file]

    return content

def score(n,gpt_ans,typ_ans):
    gpt_score = 0
    typ_score = 0
    answer = []

    data = load_data(n)
    for content in data:
        answer.append(content["answer"])
    
    for i in range(len(answer)):
        if answer[i] == gpt_ans[i]:
            gpt_score += 1
        if answer[i] == typ_ans[i]:
            typ_score += 1
    print(f"ChatGPT performed {gpt_score}/{len(answer)}")
    print(f"Typhoon performed {typ_score}/{len(answer)}")


    return


if __name__ == "__main__":

    # MCQ 1
    gpt_ans = ["a","e","a","a","e","b","c","b","c","b","b","a","b","b","b","c","c","b","a","b","b","a","a","b","b","c","a","b","d","a","c","a","c","b","c","c"]
    typ_ans = ["a","e","b","a","e","b","c","b","c","b","c","a","b","b","b","b","c","b","d","b","e","a","b","b","b","a","b","c","d","a","c","a","c","c","c","c"]
    
    score(1,gpt_ans,typ_ans)

    # MCQ 2
    gpt_ans = ["a","b","b","a","b","a","a","b","c","b","a","a","c","b","c","b","b","b","b","c","c","b","b","b","b","c","b","b","b","a","b","b","c","b","b","c"]
    typ_ans = ["d","a","e","a","d","a","a","b","c","b","e","c","b","b","e","b","b","b","b","c","c","b","d","b","b","d","e","b","b","a","d","b","c","b","c","c"]
    
    score(2,gpt_ans,typ_ans)

