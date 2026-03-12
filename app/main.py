from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import inquiry

app = FastAPI(title="M3GAN AI Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(inquiry.app_router)

@app.get("/")
async def root():
    return {"message": "M3GAN AI API is online"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)