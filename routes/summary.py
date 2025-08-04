from fastapi import APIRouter
from sqlalchemy import select

from data import database, Game

router = APIRouter()


@router.get("/summary")
async def get_summary():
    query = select(Game)
    games = await database.fetch_all(query)
    game_dicts = [dict(game) for game in games]

    if not game_dicts:
        return {"message": "No data available"}

    summary = {}
    total = len(game_dicts)
    summary["total_games"] = total

    vs_ai_count = sum(1 for game in game_dicts if game['vs_ai'])
    summary["vs_ai_percent"] = round((vs_ai_count / total) * 100, 2)
    summary["vs_human_percent"] = round(100 - summary["vs_ai_percent"], 2)

    x_wins = sum(1 for game in game_dicts if game['result'] == "X")
    o_wins = sum(1 for game in game_dicts if game['result'] == "O")
    draws = sum(1 for game in game_dicts if game['result'] == "draw")
    summary["results"] = {
        "x": round((x_wins / total) * 100, 2),
        "o": round((o_wins / total) * 100, 2),
        "draw": round((draws / total) * 100, 2),
    }

    modes = set(game['mode'] for game in game_dicts)
    summary["by_mode"] = {}

    for mode in modes:
        mode_games = [game for game in game_dicts if game['mode'] == mode]
        total_mode = len(mode_games)
        durations = [game['duration_ms'] for game in mode_games]
        move_counts = [game['move_count'] for game in mode_games]

        summary["by_mode"][mode] = {
            "game_count": total_mode,
            "avg_duration_ms": round(sum(durations) / total_mode),
            "max_duration_ms": max(durations),
            "min_duration_ms": min(durations),
            "avg_move_count": round(sum(move_counts) / total_mode),
            "max_move_count": max(move_counts),
            "min_move_count": min(move_counts),
        }

    return summary
