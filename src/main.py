from fastapi import FastAPI
from src.api.social_api import router

app = FastAPI()

app.include_router(
    prefix="/api/social",
    router=router
)