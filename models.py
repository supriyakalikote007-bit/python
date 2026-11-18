## backend model goes here....

import os
from google import genai

api_key = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key = api_key)

def gemini(prompt):
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text