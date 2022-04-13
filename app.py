from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.auth import auth_router

from db import models
from db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Escuela Para Padres", version="0.3.0")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.post("/auth/signin")
# def sign_in():
#     return {"accessToken": "Hola mundo"}


app.include_router(auth_router)
