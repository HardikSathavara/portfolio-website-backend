from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.inqury.inqury_schemas import InquiryCreate, InquiryResponse
from app.inqury.inqury_services import gs_service

router = APIRouter(prefix="/inquiries", tags=["Inquiries"])

@router.post("/submit", response_model=InquiryResponse)
async def submit_inquiry(inquiry: InquiryCreate, background_tasks: BackgroundTasks):
    if not gs_service.sheet:
        raise HTTPException(status_code=503, detail="Google Sheets service not available")
    
    try:
        # Run the slow network call in the background
        background_tasks.add_task(gs_service.append_inquiry, inquiry)
        
        return {
            "status": "success", 
            "message": "Inquiry received. Data is being saved."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))