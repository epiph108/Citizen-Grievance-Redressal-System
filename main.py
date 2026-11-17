from fastapi import FastAPI
from routers import complaints, departments
from config import settings

app = FastAPI()

app.include_router(complaints.router)
app.include_router(departments.router)

@app.get("/")
def demo():
    return {"message": "Citizen Grievance Redressal System is running"}

@app.get("/config")
def config_info():
    return {
        "app_name": settings.app_name,
        "token_expiry": settings.access_token_expire_minutes
    }