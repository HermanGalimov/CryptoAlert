from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class Coin(Base):
    __tablename__ = "coins"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    name = Column(String)
    rules = relationship("Rule", back_populates="coin")

class Rule(Base):
    __tablename__ = "rules"
    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coins.id"))
    type = Column(String)  # "above", "below", "pct_change"
    value = Column(Float)
    cooldown_minutes = Column(Integer, default=5)
    active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    coin = relationship("Coin", back_populates="rules")

class Tick(Base):
    __tablename__ = "ticks"
    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coins.id"))
    price = Column(Float)
    collected_at = Column(DateTime, default=datetime.utcnow)
