from typing import List
from pydantic import BaseModel



class LoginRequest(BaseModel):
    email:str
    password:str

class LoginResponse(BaseModel):
    message:str
    result:list=None

class DoctorRegisterRequest(BaseModel):
    name:str
    email:str
    password:str

class TokenRequest(BaseModel):
    token:str

