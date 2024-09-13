import os
from dotenv import load_dotenv

load_dotenv(".envrc")
# load_dotenv(".env")

API_KEY = os.getenv("API_KEY", "")
MODEL = "typhoon-v1.5x-70b-instruct"
BASE_URL= "https://api.opentyphoon.ai/v1"
# REPETITION_PENALTY = 1.05
MAX_TOKENS = 500