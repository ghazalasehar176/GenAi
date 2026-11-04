
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

for i in range(3):
    question = input(f"Question {i + 1}/3: ")
    response = client.responses.create(
    input=question,
    model="openai/gpt-oss-20b",
)
    print(response.output_text)
print()