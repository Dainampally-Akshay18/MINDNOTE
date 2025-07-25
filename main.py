from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

conn=MongoClient("mongodb://localhost:27017/MINDNOTE")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
print()
@app.get("/")
def homed(request: Request):
    docs = conn.MINDNOTE.NOTE.find()  # NOTE is uppercase as per your DB
    newDocs = []
    for doc in docs:
        print("Updated Document", doc)
        newDoc = {
            "id": str(doc["_id"]),
            "note": doc.get("notes", ""),  # use .get for safety
        }
        newDocs.append(newDoc)
    return templates.TemplateResponse("index.html", context={"request": request, "newDocs": newDocs})

@app.get("/about-us")
def aboutus(request: Request):
    return templates.TemplateResponse("about.html", context={"request": request})