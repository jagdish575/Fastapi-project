from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="Notification API",
    description="""
    ## 🚀 Notification API
    This API allows you to **manage notifications** efficiently.

    ### Features:
    - 📩 Create a notification
    - 🔄 Update a notification
    - 📋 Get all notifications
    - ✅ Enable or disable notifications
    - ❌ Delete notifications

    🔍 **Use the endpoints below to interact with the API!**
    """,
    version="1.0",
    contact={
        "name": "xyz",
        "email": "your-email@example.com",
        "url": "https://your-website.com"   
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)
