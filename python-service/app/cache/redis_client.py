import os
import redis
from redis import Redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

def getRedisClient() -> Redis:
    return redis.from_url(
        REDIS_URL,
        decode_responses=True
    )