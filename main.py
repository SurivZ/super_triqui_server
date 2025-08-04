from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data import register_events
from routes import register_routes

app = FastAPI()

app.title = "Super Triqui API"
app.description = "API for Super Triqui game, handling game creation, summaries, and game retrieval."
app.version = "0.1.0-beta"
app.contact = {
    "name": "David Serrano",
    "email": "franklinserrano23@gmail.com",
    "github": "https://github.com/SurivZ",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_events(app)

register_routes(app)
