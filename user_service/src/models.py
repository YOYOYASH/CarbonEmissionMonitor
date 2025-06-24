from sqlalchemy import Boolean, Column, Date, Float, Integer, String, ForeignKey, DATE,BigInteger,TIMESTAMP, Text, func
from src.dependencies.database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, index = True)
    username = Column(String,index=True,nullable=False)
    email = Column(String,index=True,unique=True,nullable=False)
    password = Column(String,nullable=False)
    present_company = Column(String,index=True,nullable=False)
    role  =Column(String,index=True,nullable=False)
    
