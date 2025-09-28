from pydantic import BaseModel
from datetime import datetime

class RuleBase(BaseModel):
    coin_symbol: str
    type: str
    value: float
    cooldown_minutes: int = 5

class RuleCreate(RuleBase):
    pass

class RuleResponse(RuleBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
