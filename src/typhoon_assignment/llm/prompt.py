SYSTEM_PROMPT = """

# Rules
Make sure the MCQ generated is in json format.
Make sure there are 5 choices a, b, c, d, and e.
Make sure there is only 1 correct answer to each question.
Make sure all text is in Thai.

# Format
The multiple choice question generated must follow a specific json format :
{{"question": Question, "a": Choice A, "b": Choice B, "c": Choice C, "d": Choice D, "e": Choice E, "answer": Correct Letter}}

# Example
{{"question": "เนื้อสัตว์ใช้ในการทำ คอหมูย่าง คืออะไร?", "a": "เนื้อไก่", "b": "เนื้อวัว", "c": "เนื้อหมู", "d": "เนื้อปลา", "e": "เนื้อกุ้ง", "answer": "c"}}
{{"question": "นำเนื้อหมูที่ผ่านการหมักครบ ลงย่างบนเตาถ่านที่เตรียมไว้ ข้อความนี้เกี่ยวข้องกับเมนูอาหารไทยอะไร?", "a": "ผัดไทย", "b": "คอหมูย่าง", "c": "เสือร้องไห้", "d": "แกงเขียวหวาน", "e": "ต้มยำกุ้ง", "answer": "b"}}

# Context
Use the provided recipe to generate the question and answers for the multiple choice questions.
The correct answer to the multiple choice question must come from the provided recipe.
## Key
dish_name : The name of this dish
desription : The description of this dish
ingredients : The ingredient of this dish
instructions : The procedure to cook this dish
\n ------- \n
All recipes : {data}
\n ------- \n
"""