from fastapi import APIRouter

router = APIRouter(tags=["users"])

@router.get("/users")
def get_users():
    return {"message": "List of all users"}

@router.get("/users/me")
def get_my_profile():
    return {"message": "My profile"}