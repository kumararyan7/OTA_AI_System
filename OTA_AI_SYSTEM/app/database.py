from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./ota.db" #simple start

#create engine = connection to database

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

#session = temporary connection to run queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
#Base= parent class for all database table
Base = declarative_base()