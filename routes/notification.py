from fastapi import APIRouter, HTTPException
from crud import get_notification_by_office


router = APIRouter(prefix="/notification", tags=["Customer Notifications"])


@router.get("/{handling_office}")
def get_notifications(handling_office: str):
    notification = get_notification_by_office(handling_office)
    if not notification:
        raise HTTPException(status_code=404, detail="NO active notification found")
    return notification
