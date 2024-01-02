from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Root endpoint returning a simple message."""
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    """Endpoint to retrieve item details."""
    return {"item_id": item_id, "query_param": query_param}
