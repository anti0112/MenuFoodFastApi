from fastapi import APIRouter, Depends, Response, status

from menu.api.docs.documentation import StuffDocs
from menu.services.service import Services, service_stub

stuff_router = APIRouter()


@stuff_router.post(
    "/stuff_db",
    tags=["stuff"],
    description=StuffDocs.POST_STUFF,
    summary=StuffDocs.POST_STUFF,
    status_code=status.HTTP_201_CREATED,
)
async def stuff_db(services: Services = Depends(service_stub)):
    await services.db_service.create_stuff_db()

    return Response(status_code=status.HTTP_201_CREATED)