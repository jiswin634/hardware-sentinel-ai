from google import genai
import json

import os

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

with open("hardware_state.json", "r") as f:
    hardware = json.load(f)

prompt = f"""
Analyze this mobile hardware data and tell me if there are risks.

Data:
{hardware}

Give:
1. Battery health analysis
2. Performance risks
3. Overheating risks
4. Recommendations
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)