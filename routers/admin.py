from fastapi import APIRouter

router = APIRouter(tags=["admin"])

@router.get("/admin/stats/departments")
def get_department_stats():
    return {"message": "Department-wise complaint count"}