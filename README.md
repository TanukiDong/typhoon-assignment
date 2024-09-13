# typhoon-assignment-1

To run this project : Add typhoon API to .envrc

```bash
.
├── README.md
├── pyproject.toml
├── requirements-dev.lock
├── requirements.lock
└── src
    └── typhoon_assignment
        ├── __init__.py
        ├── data
        │   ├── mcq1.jsonl              → First set of MCQ
        │   ├── mcq2.jsonl              → Second set of MCQ
        │   ├── recipe.json             → Fixed recipe data
        │   ├── recipe_scrape.json      → Raw recipe data from website
        │   └── thai_test_example.jsonl → Example format of MCQ
        ├── grade.py                    → Check answer with GPT
        ├── llm
        │   ├── __init__.py             → Initialize Typhoon
        │   └── prompt.py               → Prompt to generate MCQ
        ├── mcq.py                      → Generate MCQ
        ├── scrape.py                   → Scrape data from website
        └── setting.py                  → Setting of this project
```

# Web Search
Scrape data from Foodpanda for Thai food recipes. The informaton includes : 
* Dish name
* Description
* Ingredients
* Instruction

# MCQ
1. Given description of a dish, what dish is it describing
2. Given a dish, what ingredient is used to make this dish
3. Given an ingredient, how much of it is needed to make a given dish
4. Given a step from the instruction, what dish does this step related to.

# Score
MCQ1
Chat performed 32/36 <br>
MCQ1
Chat performed 34/36

# Issue / Remarks
1. Accessing Web
    * Can't access website with  requests.get(url).content <!-- Follow https://medium.com/@thunderguy/มาทำ-web-scraping-โดยใช้-beautifulsoup-กัน-56ae5dc3e2a2 -->
    * The website is protected against bot
        * Use selenium to access webbrowser instead
    * Selenium access denied due to bot
        * Random 5-10 sleep time, random scrolling
2. Typo
    * The website got few typo 
        * eg. ผัดไทย → ไข่เป็ด 2 ฟอ''" , พริกป่น (ตามชอบ)ะ
    * Got to fix some dish name
        * สูตรผัดไทย → ผัดไทย
        * This part is manual
3. MCQ Generation
    * Result is not always in json format
    * Sometime questions are phrased ambiguously, leading to more than 1 possible answer
    * Answers are somewhat random due to using llm and randomization in the algorithm