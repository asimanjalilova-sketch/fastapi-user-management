import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

from fastapi import FastAPI, HTTPException
import grpc

from app.grpc import user_pb2
from app.grpc import user_pb2_grpc

from app.models import User

app = FastAPI()
users = {}
channel= grpc.insecure_channel("localhost:50051")
stub = user_pb2_grpc.UserServiceStub(channel)

@app.get("/")
def root():
    return {"message" : "Hello FastAPI"}

@app.get("/users/{id}")
def get_user(id : int):
    if id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return users[id]

@app.post("/users", status_code=201)
def create_user(user: User):
    if user.id in users:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )
    
    users[user.id] = {
        "id" : user.id,
        "username" : user.username
    }

    return users[user.id]

@app.get("/users")
def get_users():
    return list(users.values()) 

@app.put("/users/{id}")
def update_user(id: int, user: User):
    if id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    users[id] = {
        "id" : id,
        "username" : user.username
    }

    return users[id]

@app.delete("/users/{id}")
def delete_user(id: int):

    if id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    deleted_user = users.pop(id)

    return {
        "message" : "User deleted",
        "user" : deleted_user
    }
