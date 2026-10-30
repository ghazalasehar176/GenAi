import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(GEMINI_API_KEY)
# client = genai.Client(api_key="GEMINI_API_KEY")

# response = client.models.generate_content(
#     model="gemini-3.8-flash",
#     contents="Why Sky Is Blue?",
# )

# print(response.text)