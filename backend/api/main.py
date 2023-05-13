from fastapi import FastAPI
import redis

app = FastAPI()
cache = redis.Redis(host="redis", port=6379)


@app.get("/")
def read_root():
    count = cache.incr("hits")
    return {f"Hello:{count}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
