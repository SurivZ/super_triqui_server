from .models import Game, MoveRecord
from .connection import database, metadata, startup, shutdown


def register_events(app):
    app.add_event_handler("startup", startup)
    app.add_event_handler("shutdown", shutdown)


__all__ = ["register_events", "Game", "MoveRecord", "database", "metadata"]
