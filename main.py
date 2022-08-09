from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'message' : "Hello World"}


@app.get("/greet/{name}")
async def root(name):
    msg = "Hello "+ name
    return {'greetings': msg}

