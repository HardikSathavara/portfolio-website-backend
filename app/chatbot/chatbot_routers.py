from fastapi import APIRouter, BackgroundTasks, HTTPException
# from app.schemas import InquiryCreate, InquiryResponse
from app.chatbot.chatbot_schemas import UserQuery, BotResponse

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])


@router.post("/ask", response_model=BotResponse)
async def ask_question(user_query: UserQuery, background_tasks: BackgroundTasks):
    
    return {
        "status":"success",
        "message": "Testing"
    }