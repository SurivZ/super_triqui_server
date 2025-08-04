from .create import router as create_router
from .games import router as games_router
from .summary import router as summary_router


def register_routes(app):
    app.include_router(create_router, prefix="/api", tags=["create"])
    app.include_router(games_router, prefix="/api", tags=["games"])
    app.include_router(summary_router, prefix="/api", tags=["summary"])


__all__ = ["register_routes"]
