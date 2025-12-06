from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services.social_services import SocialService
from src.models.social_model import SocialModel

router = APIRouter()
@router.get("/socials", response_model=list[SocialModel])
def get_all_socials(db: Session = Depends(get_db)):
    service = SocialService(db)
    return service.get_all_socials()    

@router.post("/socials", response_model=SocialModel)
def create_social(social_data: dict, db: Session = Depends(get_db)):
    service = SocialService(db)
    return service.create_social(social_data)

@router.get("/socials/user/{user_id}", response_model=list[SocialModel])
def get_socials_by_user_id(user_id: str, db: Session = Depends(get_db)):
    service = SocialService(db)
    return service.get_socials_by_user_id(user_id)