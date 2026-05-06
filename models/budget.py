from sqlalchemy import Column, Integer, Float, ForeignKey
from backend.database import Base

class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True)
    income = Column(Float)
    expenses = Column(Float)
    goals = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
