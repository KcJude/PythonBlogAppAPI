from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



#Database and SQLALCHEMY connection
SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker( bind=engine, autocommit=False, autoflush=False,)


#Database declaration
Base = declarative_base()