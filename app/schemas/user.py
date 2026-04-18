


from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# What we receive when user REGISTERS
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"  # default role is user
    manager_id: Optional[int] = None

# What we SEND BACK (never send password)
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# What we receive when user LOGS IN
class UserLogin(BaseModel):
    email: EmailStr
    password: str