from pydantic import BaseModel
from starlette.responses import Response as BaseResponse
from datetime import datetime
class NotificationCreate(BaseModel):
    handling_office: str
    content: str


class NotificationUpdate(BaseModel):
    handling_office: str
    content: str
    is_active: bool

class NotificationResponse(BaseModel):
    id: int
    handling_office: str
    content: str
    is_active: bool




