from fastapi import APIRouter

router = APIRouter(tags=["departments"])

@router.get("/departments")
def get_departments():
    return {"message": "List of all departments"}