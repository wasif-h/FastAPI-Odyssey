from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"Message": "Hello World"}

@app.get('/about')
def info():
    return {'Message': "This is the about section"}

