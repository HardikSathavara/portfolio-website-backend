from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routers import inquiry
from app.services import gs_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs on Startup
    gs_service.connect()
    yield
    # This runs on Shutdown
    print("Server shutting down...")

app = FastAPI(title="M3GAN AI API", lifespan=lifespan)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(inquiry.router)

@app.get("/")
async def root():
    return {"message": "M3GAN AI API is running"}