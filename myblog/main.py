from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter, Form
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated

app = FastAPI()

# app.include_router(app, prefix="/home", tags=["Home Page"])
# app.include_router(app, prefix="/blog", tags=["Blog"]) 

#To connect to Database 
models.Base.metadata.create_all(engine)

#Database function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


@app.get('/')
def welcome():
    return 'This is Onyeuwk Blog API'
#Home Page
@app.get('/home')
def home_page():
    return 'Welcome to Onyeukwu Blog App API'  

#About Page
@app.get('/home/about')
def about_page():
    return 'This is all you need to know about Onyeukwu Blog App'  

#Contact Page
@app.get('/home/contact')
def contact_page():
    return 'You can contact the Administrators and Creators of Onyeukwu Blog App here'


#Create blog
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data": "New Blog created successfully", "blog": new_blog}


#To delete a blog by ID
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"data": "Blog with id {id} deleted successfully"}
    

#To get/show the blogs created
@app.get('/blog', status_code=status.HTTP_200_OK)
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


#Search Through Blogs by ID
@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog_by_id(id, response: Response, db: Session = Depends(get_db)):
     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
     if not blog: 
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} not found")
     return blog
 

#Update Blog Title and Body with The Blog ID
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found in our database")
    blog.update(request.dict())
    db.commit()
    return {"Data": "New Blog Updated Successfully"}

#Create New User
@app.post('/user', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.Users, db: Session = Depends(get_db)):
    new_user = models.User(first_name=request.first_name, last_name=request.last_name, email=request.email, username=request.username, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"Message": "New User created successfully", "Data": new_user}


#User Login
@app.post('/user/user_login', status_code=status.HTTP_200_OK)
def user_login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return {"Message": "User Login Successfull", "username": username, "password": password}

#Edit Blog by User/Author
@app.put("blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def user_edit_blog(id, request: schemas.Users, db: Session = Depends(get_db)): 
    user = db.query(models.User)(models.Blog).filter(models.User.user_id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{user_id} entered did not match any Blog with id {id} in our database to be edited")
    user.update(request.dict())
    db.commit()
    return {"Message": "User author successfully edited his Blog", "data": blog}

