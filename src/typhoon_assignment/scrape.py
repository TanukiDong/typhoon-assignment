# import requests
from bs4 import BeautifulSoup
import html
from selenium import webdriver
import json
import time
import random
from pathlib import Path

def scrape(url):
    # Selenium
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(random.uniform(10, 15)) # Not a Bot!
    driver.execute_script(f"window.scrollTo(0,{random.uniform(1000, 3000)})")  # Not a Bot!
    page_content = driver.page_source

    # BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    time.sleep(random.uniform(10, 15)) # Not a Bot!
    
    driver.quit()

    # # Read Content after defining recipe_section
    # line_count = 0
    # for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'a', 'li']):
    #     text = element.get_text()
    #     decoded_text = html.unescape(text)
    #     if line_count < 45:
    #         print(decoded_text)
    #         time.sleep(0.1)
    #         line_count += 1
    #     else:
    #         break
    

    recipe = {
        "dish_name": "",
        "description" : "",
        "ingredients": [],
        # 'cooking_time': '',
        # 'tools': [],
        "instructions": []
    }
    recipe_section = soup.find('div', id='recipes')

    # Dish Name
    dish_name_section = soup.find('h1')
    recipe['dish_name'] = dish_name_section.text.strip() if dish_name_section else ''

    # Description
    description_section = recipe_section.find('span')
    recipe['description'] = description_section.text.strip() if description_section else ''

    # # Cooking Time
    # cooking_time_section = recipe_section.find('strong', string='ระยะเวลาทำอาหาร')
    # cooking_time_data = cooking_time_section.find_next('time') if cooking_time_section else None
    # recipe['cooking_time'] = cooking_time_data.text.strip() if cooking_time_data else ''

    # Ingredient
    ingredients_section = recipe_section.find('h2', string='วัตถุดิบ')
    ingredients_list = ingredients_section.find_next('ul') if ingredients_section else None
    recipe['ingredients'] = [li.text.strip() for li in ingredients_list.find_all('li')] if ingredients_list else []

    
    # Tool
    # tools_section = recipe_section.find('h2', string='อุปกรณ์ที่ใช้ในการประกอบอาหาร')
    # tools_list = tools_section.find_next('ul') if tools_section else None
    # recipe['tools'] = [li.text.strip() for li in tools_list.find_all('li')] if tools_list else []

    
    # Instruction
    instructions_section = recipe_section.find('h2', string='ขั้นตอนการทำ')
    instructions_list = instructions_section.find_next('ul') if instructions_section else None
    recipe['instructions'] = [li.text.strip() for li in instructions_list.find_all('li')] if instructions_list else []
    
    return recipe

if __name__ == "__main__":
    urls = [
        "https://www.foodpanda.co.th/contents/pad-thai-recipe", # ผัดไทย
        "https://www.foodpanda.co.th/contents/spicy-beef-salad-recipe", # ยำเนื้อ
        "https://www.foodpanda.co.th/contents/thai-basil-pork-recipe", # ผัดกะเพราหมู
        "https://www.foodpanda.co.th/contents/tom-yum-goong-recipe", # ต้มยำกุ้ง
        "https://www.foodpanda.co.th/contents/tom-kha-gai-recipe", # ต้มข่าไก่
        "https://www.foodpanda.co.th/contents/green-papaya-salad-recipe", # ส้มตำ
        "https://www.foodpanda.co.th/contents/gaeng-kiaw-wan-recipe", # แกงเขียวหวาน
        "https://www.foodpanda.co.th/contents/drunken-noodles-recipe", # ผัดขี้เมา
        "https://www.foodpanda.co.th/contents/crying-tiger-recipe", # เสือร้องไห้
        ]
    
    db = []

    for url in urls:
        recipe_data = scrape(url)
        db.append(recipe_data)
        if url != urls[-1]:
            time.sleep(random.uniform(45, 60)) # Not a Bot!

    # Print
    for content in db:
        print(json.dumps(content, ensure_ascii=False, indent=4))

    DATA_DIR = Path(__file__).parent / "data/recipe_scrape.json"
    with open(DATA_DIR, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)