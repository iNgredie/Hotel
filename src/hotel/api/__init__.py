from fastapi import APIRouter

from .booking import router as booking_router
from .role import router as role_router
from .room import router as room_router
from .user import router as user_router


router = APIRouter()
router.include_router(booking_router)
router.include_router(role_router)
router.include_router(room_router)
router.include_router(user_router)
