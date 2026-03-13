from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from app.chatbot.chatbot_schemas import UserQuery, BotResponse
from app.chatbot.rag.handler import handle_query


router = APIRouter(prefix="/chatbot", tags=["Chatbot"])


@router.post("/ask", response_model=BotResponse)
async def ask_question(user_query: UserQuery, request: Request, background_tasks: BackgroundTasks):
    
    response = handle_query(user_query.query, request)

    print('=============response===============', response, type(response))
    
    return {
        "status":"success",
        "message": response
    }