import os
from dotenv import load_dotenv

load_dotenv(".envrc")
# load_dotenv(".env")

API_KEY = os.getenv("API_KEY", "")
MODEL = "typhoon-instruct"
BASE_URL= "https://api.opentyphoon.ai/v1"
