from pydantic import BaseModel
from typing import Optional

class LocationRequest(BaseModel):
    latitude: float
    longitude: float
    message: Optional[str] = None   # 👈 ADD THIS
