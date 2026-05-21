import json
import os
from datetime import datetime

LOG_PATH = "data/game_logs.json"
STATS_PATH = "data/player_stats.json"

class PersistenceManager:
    @staticmethod
    def ensure_files():
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(LOG_PATH):
            with open(LOG_PATH, "w") as file:
                json.dump([], file)

        if not os.path.exists(STATS_PATH):
            with open(STATS_PATH, "w") as file:
                json.dump({}, file)

    @staticmethod
    def load_logs():
        with open(LOG_PATH, "r") as file:
            return json.load(file)

    @staticmethod
    def save_logs(logs):
        with open(LOG_PATH, "w") as file:
            json.dump(logs, file, indent=4)

    @staticmethod
    def add_log(winner, loser, result):
        logs = PersistenceManager.load_logs()

        logs.append({
            "winner": winner,
            "loser": loser,
            "result": result,
            "timestamp": str(datetime.now())
        })

        PersistenceManager.save_logs(logs)

    @staticmethod
    def clear_logs():
        PersistenceManager.save_logs([])

    @staticmethod
    def remove_last_game():
        logs = PersistenceManager.load_logs()

        if logs:
            logs.pop()

        PersistenceManager.save_logs(logs)

    @staticmethod
    def load_stats():
        with open(STATS_PATH, "r") as file:
            return json.load(file)

    @staticmethod
    def save_stats(stats):
        with open(STATS_PATH, "w") as file:
            json.dump(stats, file, indent=4)

    @staticmethod
    def register_win(winner, loser):
        stats = PersistenceManager.load_stats()

        if winner not in stats:
            stats[winner] = {
                "wins": 0,
                "against": {}
            }

        stats[winner]["wins"] += 1

        if loser not in stats[winner]["against"]:
            stats[winner]["against"][loser] = 0

        stats[winner]["against"][loser] += 1

        PersistenceManager.save_stats(stats)