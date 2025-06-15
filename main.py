from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_a():
    return "A"
