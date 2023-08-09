from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime



class DirectorSchema(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr | None = None
    Active_time : datetime
    Create_time : datetime
    boss_id: int
    pre_director_id: int
    workers_id: int

    class Config:
        orm_mode = True


class BossSchema(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr | None = None
    Active_time : datetime
    Create_time : datetime
    workers_id: int

    class Config:
        orm_mode = True


class Pre_DirectorSchema(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr | None = None
    Active_time : datetime
    workers_id: int

    class Config:
        orm_mode = True  


class WorksSchema(BaseModel):
    name : str
    join_data : datetime
    complete_data : datetime
    status : str
    price : int
    employer : str
    worker : str


class WorkersSchema(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr | None = None
    Active_time : datetime
    Create_time : datetime   


class UserSchema(BaseModel):
    role : str
    username : str
    password: str
  

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None    