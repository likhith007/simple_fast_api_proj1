from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'message': "Hello World"}


@app.get("/greet/{name}")
async def root(name):
    msg = "Hello " + name
    return {'greetings': msg}


@app.get("/bye/{name}")
async def say_bye(name):
    bye_msg = "Bye " + name
    return {'greet': bye_msg}
