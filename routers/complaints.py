from fastapi import APIRouter

router = APIRouter(tags=["complaints"])

@router.get("/complaints")
def get_complaints():
    return {"message": "List of all complaints"}