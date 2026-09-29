from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()

SYSTEM_PROMPT = """You are the virtual host for {name}, a restaurant located at {address}.
You are open from {opening_time} to {closing_time}.

Be warm, concise, and conversational.
"""

RESTAURANT_INFO = {
    "name": "The Coastal Grill",
    "address": "123 Harbor Drive, San Diego, CA",
    "opening_time": "11:00",
    "closing_time": "22:00",
}

system_message = SYSTEM_PROMPT.format(**RESTAURANT_INFO)

api_key = os.getenv("GROQ_API")
if not api_key:
    raise RuntimeError("Groq Api does'nt exists please check your .env")

client = Groq(api_key=api_key)

def get_response(db,message : str):
    messages = [{"role" : "system","content" : system_message},
               {"role" : "user", "content" : message}] 
    response = client.chat.completions.create(
        message = messages,
        model="openai/gpt-oss-120b",  
    )

    final_answer = response.choices[0].message.content
    return final_answer

print(get_response(None,"hey what time do you open?"))