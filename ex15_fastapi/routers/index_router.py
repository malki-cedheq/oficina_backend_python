from fastapi import APIRouter, status

index_router = APIRouter()


@index_router.get("/", status_code=status.HTTP_200_OK)
async def index():
    return {"message": "Hello Wordl"}
