from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
import datetime

class Doctor(BaseModel):
    id:Optional[int]
    name:str
    email:str
    password:str
    dept:str

    def tuple_for_insert(self):
        return (self.name,self.email,self.password,self.dept,)

class Patient(BaseModel):
    id:Optional[int]
    name:str
    email:str
    password:str
    doc_id:Optional[int]

    def tuple_for_insert(self):
        return (self.name,self.email,self.password,self.doc_id,)

class Record(BaseModel):
    id:int
    age:int=0
    sex:int=0
    cp:int=0
    trestbps:int=0
    chol:int=0
    fbs:int=0
    restecg:int=0
    thalach:int=0
    exang:int=0
    oldpeak:Decimal=0
    slope:int=0
    ca:int=0
    thal:int=0
    target:Optional[int]
    date:str = str(datetime.date.today())
    time:str = str(datetime.datetime.now().strftime("%H:%M:%S"))

    def tuple_for_insert(self):
        return (self.id,self.age,self.sex,self.cp,self.trestbps,self.chol,self.fbs,self.restecg,
        self.thalach,self.exang,self.oldpeak,self.slope,self.ca,self.thal,self.target,self.date,self.time,)

class TokenRequest(BaseModel):
    token:str
# data ={
#     "id":1,
#    "age": 52,
#    "sex": 1,
#    "cp": 0,
#    "trestbps": 125,
#    "chol": 212,
#    "fbs": 0,
#    "restecg": 1,
#    "thalach": 168,
#    "exang": 0,
#    "oldpeak": 1.34,
#    "slope": 2,
#    "ca": 2,
#    "thal": 3
 
#  }
# print(Record(**data))