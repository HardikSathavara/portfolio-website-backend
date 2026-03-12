from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.schemas import InquiryCreate, InquiryResponse
from app.services import gs_service

app_router = APIRouter(
    prefix="/inquiries",
    tags=["Inquiries"]
)

@app_router.post("/submit", response_model=InquiryResponse)
async def submit_inquiry(inquiry: InquiryCreate, background_tasks: BackgroundTasks):
    try:
        # background_tasks.add_task runs the Google API call 
        # AFTER sending the response to the user for speed.
        background_tasks.add_task(gs_service.append_inquiry, inquiry)
        
        return {"status": "success", "message": "Inquiry received and is being saved."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Google Sheets Error: {str(e)}")