# %%
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdateRequest
from typing import List
from uuid import UUID

app = FastAPI()

db: List[User] = [
        User(
                id = UUID("974a1a31-173e-4ac2-a55c-44c538664da1"), 
                first_name = "Rachel", 
                last_name = "Hill",
                gender = Gender.female,
                roles = [Role.student]
             ),
        User(
                id = UUID("6e083141-3416-428f-be20-284aa117d499"), 
                first_name = "Luke", 
                last_name = "Tutton",
                gender = Gender.male,
                roles = [Role.user]
             )
]

@app.get("/")
async def root():
        return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
        return db

@app.post("/api/v1/users")
async def register_user(user: User):
        db.append(user)
        return {"id" : user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
        for user in db:
                if user.id == user_id:
                        db.remove(user)
                        return
        raise HTTPException(
                status_code = 404,
                detail = f"User with id: {user_id} does not exist."
        )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: UserUpdateRequest):
        for user in db:
                if user.id == user_id:
                        if user_update.first_name != None:
                                user.first_name = user_update.first_name
                        if user_update.last_name != None:
                                user.last_name = user_update.last_name
                        if user_update.middle_name != None:
                                user.middle_name = user_update.middle_name
                        if user_update.roles != None:
                                user.roles = user_update.roles
                        return
        raise HTTPException(
                status_code = 404,
                detail = f"User with id: {user_id} does not exist."
        )