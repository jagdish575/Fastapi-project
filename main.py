from fastapi import FastAPI
from routes import notification,admin_notification
from metadata import app


app.include_router(notification.router)
app.include_router(admin_notification.router)


@app.get("/")
def default_api():
    return { "message" : "Notification Service is running"}