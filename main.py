from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'data':{'name': 'My Blogging App'}}


@app.get('/about')
def about():
    return {'data':{'This is all the Blogging App'}}