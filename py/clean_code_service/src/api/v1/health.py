from fastapi import APIRouter

from models.health_models import GetHealth


router = APIRouter(prefix="/health", tags=["health"])

@router.get("")
def get_health() -> GetHealth:
    return GetHealth(
        status="Ok",
        message="App is running",
    )
