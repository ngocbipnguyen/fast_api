from pydantic import BaseModel
from typing import  List
from .collection import Collection

class Profile(BaseModel):
    id: str
    total_views: int
    all_time_rank: int
    month_rank: int


class Social(BaseModel):
    id: str
    name: str
    icon_url: str
    link: str
    user_id: str
    class Config:
        orm_mode = True

class User(BaseModel):
    id: str
    name: str
    username: str
    photo_url: str
    email: str
    token: str
    time_login: int
    follow: bool
    is_active: bool
    
    profile: Profile
    collections: List[Collection] = []
    social: List[Social] = []

    class Config:
        orm_mode = True