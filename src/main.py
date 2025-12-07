from fastapi import FastAPI
from src.api.social_api import router
from src.api.user_api import user_router
from src.api.collection_api import collection_router
from src.api.pixel_photo_api import photo_router

app = FastAPI()

app.include_router(
    prefix="/api/social",
    router=router
)

app.include_router(
    prefix="/api/user",
    router=user_router
)


app.include_router(
    prefix="/api/collection",
    router=collection_router
)


app.include_router(
    prefix="/api/photo",
    router=photo_router
)