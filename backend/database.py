from gc import collect
from model import Todo

# MongoDB driver
import motor.motor_asyncio

# This declares a connection between database.py to
# MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

# A database TodoList is specified in Mongodb
database = client.TodoList
# A collection (table) within TodoList
collection = database.todo

# Fetch Todo
async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

# Fetch all todos
async def fetch_all_todos() -> list:
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

# Create todo
async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

# Update todo
async def update_todo(title, desc):
    # Mongodb will find the item to update by the first param
    # i.e. title
    await collection.update_one({"title": title}, {"$set":{
        "description":desc}})
    document = await collection.find_one({"title":title})
    return document

# Delete Todo
async def remove_todo(title) -> bool:
    document = await fetch_one_todo(title)
    if not document:
        return False
    await collection.delete_one({"title":title})
    return True
