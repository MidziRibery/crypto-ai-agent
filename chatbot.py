from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

# Set OpenAI API key
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model='gpt-4o-mini',
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(completion.choices[0].message);