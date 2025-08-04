from fastapi import APIRouter, status
from sqlalchemy import select

from data import database, Game, MoveRecord

router = APIRouter()


@router.get("/games", status_code=status.HTTP_200_OK)
async def get_games():
    query = select(Game)
    games = await database.fetch_all(query)
    return [dict(game) for game in games]


@router.get("/game/{game_id}", status_code=status.HTTP_200_OK)
async def get_game_by_id(game_id: int):
    game = await database.fetch_one(select(Game).where(Game.id == game_id))
    if not game:
        return {"error": "Game not found"}, status.HTTP_404_NOT_FOUND

    moves = await database.fetch_all(select(MoveRecord).where(MoveRecord.game_id == game_id))

    return {
        "game": dict(game),
        "moves": [dict(move) for move in moves]
    }
