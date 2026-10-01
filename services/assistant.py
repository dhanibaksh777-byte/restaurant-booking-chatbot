from groq import Groq
from tools.menu_lookup import menu_lookup,menu_lookup_tool
from dotenv import load_dotenv
from model import Conversation,Message
from sqlalchemy.orm import Session
import json
import os


load_dotenv()


SYSTEM_PROMPT = """You are the virtual host for {name}, a restaurant located at {address}.
You are open from {opening_time} to {closing_time}.

You have access to a menu_lookup tool. Use it whenever a customer asks about dishes, menu categories, or prices. Never invent menu items or prices — always look them up.

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

def get_response(db  : Session,message : str,conversation_id : str):

    if not conversation_id:
        new_conv = Conversation()
        db.add(new_conv)
        db.commit()
        conversation_id = new_conv.id

    new_message = Message(conversation_id = conversation_id,role = "user",content = message)
    db.add(new_message)
    db.commit()

    history = db.query(Message).filter(Message.conversation_id == conversation_id).order_by(Message.created_at).all()
    messages = [{"role": "system", "content": system_message}]
    for h in history:
        messages.append({"role" : h.role,"content" : h.content})



    while True:

        response = client.chat.completions.create(
            messages=messages,
            model="openai/gpt-oss-120b",
            tools=[menu_lookup_tool]
        )

        tool_calls = response.choices[0].message.tool_calls
        if not tool_calls:
            final_text = response.choices[0].message.content
            db.add(Message(conversation_id=conversation_id, role="assistant", content=final_text))
            db.commit()
            return final_text, conversation_id

        messages.append(response.choices[0].message)
        for tool_call in tool_calls:
            arguments  = json.loads(tool_call.function.arguments)
            result = menu_lookup(db, **arguments)
            messages.append({"role" : "tool", "tool_call_id" : tool_call.id, "content" : str(result)})


from database import SessionLocal
db = SessionLocal()
reply1, conv_id = get_response(db, "what mains do you have?", None)
print("Bot:", reply1)
reply2, conv_id = get_response(db, "tell me more about the salmon", conv_id)
print(reply2)