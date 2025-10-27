# web/main.py
from fastapi import FastAPI
import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "web service up"}

@app.get("/visits")
def visits():
    # increment counter in Redis and return value
    try:
        count = r.incr("visits")
        return {"visits": int(count)}
    except Exception as e:
        return {"error": str(e)}
