from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.inqury.inqury_services import gs_service
from app.inqury import inqury_routers
from app.chatbot import chatbot_routers
from app.chatbot.rag.llm_manager import LLMManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs on Startup
    gs_service.connect()

    app.state.llm_manager = LLMManager()

    print("LLM initialized")
    
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
app.include_router(inqury_routers.router)
app.include_router(chatbot_routers.router)

@app.get("/")
async def root():
    return {"message": "M3GAN AI API is running"}