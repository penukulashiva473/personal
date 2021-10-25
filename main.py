from fastapi import FastAPI
import fastapi

app = FastAPI()

@app.post('/')
def all():
    return "Hello"