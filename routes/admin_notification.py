from fastapi import APIRouter
from schemas import NotificationResponse,NotificationUpdate,NotificationCreate
from typing import List
from crud import (
    get_all_notifications,
    create_notifications,
    update_notification,
    disable_notification,
    enable_notification,
    delete_notification,
)
router = APIRouter(prefix="/admin", tags=["Admin Notifications"])

@router.get("/notifications", response_model=List[NotificationResponse])
def list_notifications():
    return get_all_notifications() 



@router.post("/notifications")
def create_notifications_endpoint(notification: NotificationCreate):
    return create_notifications(notification)



@router.put("/notifications/{notification_id}")
def Update_notifications(notification_id: int, notification: NotificationUpdate):
    return update_notification(notification_id, notification) 


@router.patch("/notifications/{id}/disable")
def deactivate_notifications(id: int):
    return disable_notification(id)


@router.patch("/notifications/{notification_id}/enable")
def activate_notifications(notification_id: int):
    return enable_notification(notification_id)


@router.delete("/notifications/{notification_id}")
def remove_notifications(notification_id: int):
    return delete_notification(notification_id)
