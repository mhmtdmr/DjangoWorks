from uuid import uuid4
from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID,uuid4
from enum import Enum

class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    uid : Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    middle_name : Optional[str]
    gender : Gender
    roles : List[Role]
    temp_token : Optional[UUID] = uuid4()



