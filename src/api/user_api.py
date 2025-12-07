from fastapi import APIRouter, Depends
from typing import List
from src.schemas.user import User
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.services.user_service import UserService

user_router = APIRouter()

@user_router.get("/users", response_model=List[User])
def get_users(db :Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_all_users()  # Assuming this method exists

@user_router.post("/users", response_model=User)
def create_user(user_data: dict, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user_data)

@user_router.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_user_by_id(user_id)