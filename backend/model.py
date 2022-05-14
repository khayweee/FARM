from pydantic import BaseModel

class Todo(BaseModel):
    """
    The data structure of a todo object
    """
    title: str
    description: str
