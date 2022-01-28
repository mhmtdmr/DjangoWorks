from uuid import UUID, uuid4
from fastapi import FastAPI,Depends
from models import Gender, User, Role
from typing import List


app = FastAPI()


db : List[User] = [
    User(uid=UUID("8b5bf5e9-7cf0-4853-9c73-16fbe7bdd228"),first_name="Mehmet",last_name="Demir",gender=Gender.male,roles = [Role.user]),
    User(uid=UUID("fef70ce7-7c30-42a0-bbde-7baac0c1abab"),first_name="Mustafa",last_name="Kılıç",gender=Gender.male,roles = [Role.admin])

]

# @app.get("/")
# async def root():
#     return {"Hi":"Guys"}

@app.get("/api/v1/users")
async def get_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"uid":user.uid}
"""
# SENT WITH THUNDER CLIENT

  {
    "first_name": "Ömer",
    "last_name": "Kılıç",
    "middle_name": "Ali",
    "gender": "male",
    "roles": [
      "user"
    ]
  }

"""

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    temp_token = uuid4()
    return {"access_token": form_data.username + '_token_'+str(temp_token)}

@app.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {"the_token": token}
