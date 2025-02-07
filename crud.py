from database import get_db_connection
from schemas import NotificationCreate, NotificationUpdate, NotificationResponse
from typing import List
from fastapi import HTTPException
from sqlite3 import IntegrityError


def get_notification_by_office(handling_office: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM notifications WHERE handling_office = ? AND is_active = 1",
        (handling_office,),
    )
    notification = cursor.fetchone()

    if not notification:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail=f"No notifications found for handling_office: {handling_office}",
        )

    conn.close()
    return dict(notification)


def get_all_notifications() -> List[NotificationResponse]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notifications")

    notifications = cursor.fetchall()
    if not notifications:
        raise HTTPException(status_code=404, detail="No notifications found.")

    column_names = [column[0] for column in cursor.description]
    notifications_dicts = [dict(zip(column_names, row)) for row in notifications]

    conn.close()
    return [
        NotificationResponse(**notification) for notification in notifications_dicts
    ]


def create_notifications(notification: NotificationCreate) -> NotificationResponse:
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO notifications (handling_office, content) VALUES (?, ?)",
            (notification.handling_office, notification.content),
        )
        conn.commit()

        notification_id = cursor.lastrowid  
        cursor.execute("SELECT * FROM notifications WHERE id = ?", (notification_id,))
        new_notification = cursor.fetchone()

        if not new_notification:
            raise HTTPException(
                status_code=500, detail="Failed to retrieve created notification"
            )

        column_names = [column[0] for column in cursor.description]
        notification_dict = dict(zip(column_names, new_notification))

    except IntegrityError:
        conn.rollback()
        raise HTTPException(
            status_code=400,
            detail="Notification creation failed due to duplicate entry or constraint violation",
        )

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        conn.close()

    return NotificationResponse(**notification_dict)


def update_notification(notification_id: int, notification: NotificationUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE notifications SET handling_office = ?, content = ?, is_active = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
        (   
            notification.handling_office,
            notification.content,
            notification.is_active,
            notification_id,
        ),
    )
    conn.commit()
    conn.close()
    return {"message": "Notification updated successfully"}


def disable_notification(notification_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE notifications SET is_active = 0 WHERE id = ?", (notification_id,)
    )
    conn.commit()
    conn.close()
    return {"message": "Notification disabled successfully"}


def enable_notification(notification_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE notifications SET is_active = 1 WHERE id = ?", (notification_id,)
    )
    conn.commit()
    conn.close()
    return {"message": "Notification enabled successfully"}


def delete_notification(notification_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM notifications WHERE id = ?", (notification_id,))
    existing_notification = cursor.fetchone()

    if not existing_notification:
        conn.close()
        raise HTTPException(status_code=404, detail="Notification not found")

    cursor.execute("DELETE FROM notifications WHERE id = ?", (notification_id,))
    conn.commit()
    conn.close()

    return {"message": "Notification deleted successfully"}
