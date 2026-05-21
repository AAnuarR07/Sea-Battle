from functools import wraps
from datetime import datetime

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Action: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper