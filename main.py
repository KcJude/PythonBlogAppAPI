from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/blog')
def home():
    return {'data':'Blog List'}


@app.get('/blog/{id}')
def show(id):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return{'data':{1,2}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return{'data': f'Blog Created Succefully as {blog.title}'}
