from fastapi import APIRouter

from .health import router as health_router
from .ts import router as ts_router

router = APIRouter(prefix="/v1")

router.include_router(health_router)
router.include_router(ts_router)
