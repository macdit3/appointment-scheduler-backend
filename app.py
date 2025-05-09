from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to the Appointment Scheduler API Test version "}

