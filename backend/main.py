from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#App Object
app = FastAPI()

#Origin
# Creating access permission from different origin
origins = ['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Crud
@app.get("/")
def read_root():
    return {"Ping": "Pong"}