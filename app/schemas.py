from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    detail: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_At: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    title: str
    detail: str
    published: bool
    id: int
    user_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1, ge=0)
