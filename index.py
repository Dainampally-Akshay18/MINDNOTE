from fastapi import FastAPI
from routes.note import note as note_router
from models.note import Note

from fastapi.staticfiles import StaticFiles


app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(note_router,)




