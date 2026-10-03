from fastapi import APIRouter,Depends
from services.assistant import get_response
from sqlalchemy.orm import Session
from database import get_db
from schemas import ChatRequest,ChatReesponse


router = APIRouter()


@router.post("/chat",response_model=ChatReesponse)
def chat(request : ChatRequest,db : Session = Depends(get_db)):
    reply,conversation_id = get_response(db,request.message,request.conversation_id)
    return ChatReesponse(reply = reply,conversation_id = str(conversation_id))
