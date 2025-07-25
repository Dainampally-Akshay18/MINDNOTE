from pydantic import BaseModel

class Note(BaseModel):
    title: str
    Description: str
    important:bool