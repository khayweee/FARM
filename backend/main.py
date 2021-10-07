from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# App object
app = FastAPI()

# Permission
origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/api/todo")
async def get_todo():
    """ Obtain all entries """
    return 1

@app.get("/api/todo{id}")
async def get_todo_by_id():
    """ Obtain an entry by id """
    return 1

@app.post("/api/todo{id}")
async def post_todo(todo):
    """ Post a new entry """
    return 1

@app.put("/api/todo{id}")
async def put_todo(id, data):
    """ update an entry """
    return 1    

@app.delete("/api/todo{id}")
async def delete_todo(id):
    """ delete an entry """
    return 1 
