import jsonschema
from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def hello() -> jsonschema:
    return {"say": "hello!"}
