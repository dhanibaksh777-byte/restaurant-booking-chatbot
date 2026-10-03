from fastapi import FastAPI
from router import chat

app = FastAPI()

app.include_router(chat.router)