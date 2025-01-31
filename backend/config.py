import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Twitter API Keys
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# print("API Key:", os.getenv("TWITTER_API_KEY"))
# print("API Secret:", os.getenv("TWITTER_API_SECRET"))
# print("Bearer Token:", os.getenv("TWITTER_BEARER_TOKEN"))
# print("Token:", os.getenv("TWITTER_ACCESS_TOKEN"))
# print("Token Secret:", os.getenv("TWITTER_ACCESS_SECRET"))

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
