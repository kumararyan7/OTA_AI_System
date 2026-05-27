from sqlalchemy import Column, String, Integer
from app.database import Base

class Device(Base):
    __tablename__ ="devices"
    device_id = Column(String,primary_key=True,index=True)


class UpdateStatus(Base):
    __tablename__ ="updates"

    device_id = Column(String,primary_key=True)
    status = Column(String)

class Logs(Base):
    __tablename__ ="logs" 

    id = Column(Integer,primary_key=True,index= True)
    device_id = Column(String)
    message = Column(String)
    