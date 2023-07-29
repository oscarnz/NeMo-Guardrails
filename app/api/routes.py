from fastapi import APIRouter

from api.endpoint.nemo import router as nemo_router

router = APIRouter(
    prefix="",
    responses={404: {"description": "Not found"}},
)

router.include_router(nemo_router)