from sqlalchemy import Boolean, ForeignKey, Integer, String, Column
from sqlalchemy.orm import relationship
from .database import Base


#Database Model for Blog details
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    date = Column(String) 
    author = Column(String)
    
#Database Model for User details    
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)