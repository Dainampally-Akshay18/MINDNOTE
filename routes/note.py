from fastapi import APIRouter,Request
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

from fastapi.templating import Jinja2Templates

note = APIRouter()


templates= Jinja2Templates(directory="templates")


@note.get("/")
def homed(request: Request):
    docs = conn.MINDNOTE.NOTE.find()
    # NOTE is uppercase as per your DB
    newDocs = []
    for doc in docs:
        print("Updated Document", doc)
        newDoc = {
            "id": str(doc["_id"]),
            "note": doc.get("notes", ""),  # use .get for safety
        }
        newDocs.append(newDoc)
    return templates.TemplateResponse("index.html", context={"request": request, "newDocs": newDocs})


@note.post("/add")
def add_note(note: Note):
    conn.MINDNOTE.NOTE.insert_one(
        {"notes": request.form.get("note", "")}  # use .get for safety
    )
    print()        