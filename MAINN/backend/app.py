from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Medicare AI backend is running"}