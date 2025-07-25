from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from bson import ObjectId

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/")
def homed(request: Request):
    docs = conn.MINDNOTE.NOTE.find()
    newDocs = []
    for doc in docs:
        print("Updated Document", doc)
        newDoc = {
            "id": str(doc["_id"]),
            "title": doc.get("title", ""),
            "description": doc.get("Description", ""),
            "important": doc.get("important", False),
            "note": f"{doc.get('title', '')} - {doc.get('Description', '')}"
        }
        newDocs.append(newDoc)
    return templates.TemplateResponse("index.html", context={"request": request, "newDocs": newDocs})

@note.post("/add")
def add_note(
    title: str = Form(...),
    Description: str = Form(...),
    important: bool = Form(False)
):
    note_data = {
        "title": title,
        "Description": Description,
        "important": important
    }
    print("Note data:", note_data)
    inserted_note = conn.MINDNOTE.NOTE.insert_one(note_data)
    print("Inserted Note:", inserted_note)
    
    return RedirectResponse(url="/?added=true", status_code=303)

@note.post("/delete/{note_id}")
def delete_note(note_id: str):
    try:
        if not ObjectId.is_valid(note_id):
            print(f"Invalid ObjectId format: {note_id}")
            return RedirectResponse(url="/?error=invalid_id", status_code=303)
            
        object_id = ObjectId(note_id)
        result = conn.MINDNOTE.NOTE.delete_one({"_id": object_id})
        
        if result.deleted_count == 1:
            print(f"Successfully deleted note with ID: {note_id}")
            return RedirectResponse(url="/?deleted=true", status_code=303)
        else:
            print(f"Note with ID: {note_id} not found")
            return RedirectResponse(url="/?error=not_found", status_code=303)
            
    except Exception as e:
        print(f"Error deleting note: {e}")
        return RedirectResponse(url="/?error=delete_failed", status_code=303)

@note.get("/about-us")
def about_us(request: Request):
    return templates.TemplateResponse("about.html", context={"request": request})