from fastapi import APIRouter, status
from sqlalchemy import insert
from pydantic import BaseModel
from typing import List

from data import database, Game, MoveRecord

router = APIRouter()


class MoveData(BaseModel):
    move_number: int
    player: str
    board_index: int
    cell_index: int
    resulted_in_board_win: bool
    resulted_in_board_draw: bool


class GameData(BaseModel):
    mode: str
    vs_ai: bool
    ai_level: str | None
    result: str
    duration_ms: int
    timestamp: int
    move_count: int
    moves: List[MoveData]


@router.post("/game", status_code=status.HTTP_201_CREATED)
async def create_game(game: GameData):
    game_id = await database.execute(
        insert(Game).values(
            mode=game.mode,
            vs_ai=game.vs_ai,
            ai_level=game.ai_level,
            result=game.result,
            duration_ms=game.duration_ms,
            timestamp=game.timestamp,
            move_count=game.move_count
        )
    )

    for move in game.moves:
        await database.execute(
            insert(MoveRecord).values(
                game_id=game_id,
                move_number=move.move_number,
                player=move.player,
                board_index=move.board_index,
                cell_index=move.cell_index,
                resulted_in_board_win=move.resulted_in_board_win,
                resulted_in_board_draw=move.resulted_in_board_draw
            )
        )

    return {"message": "Game and moves recorded successfully"}
