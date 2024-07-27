from groq import Groq
from dotenv import load_dotenv
import os
from groq_api.system_prompt import system_prompt

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)

def generate_roast(resume_text):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        # model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": resume_text
            }
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        stream=True,
        stop=None,
    )

    roast = ''
    for chunk in completion:
        roast += chunk.choices[0].delta.content or ""

    print(roast)
    return roast