from sqlalchemy import Column, Integer
from app.database import Base

class Hotels(Base):
    __tablename__ = "Hotels"

    id = Column(Integer, primary_key=True)
    

