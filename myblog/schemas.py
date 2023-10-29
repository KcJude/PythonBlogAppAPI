from pydantic import BaseModel


#Blog Details
class Blog(BaseModel):
    title: str
    body: str
    date: str
    author: str


#User Details
class Users(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    
