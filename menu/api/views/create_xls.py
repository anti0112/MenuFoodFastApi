from fastapi import APIRouter, Depends, status

from menu.api.docs.documentation import CreateXLSLDocs
from menu.api.schemas.task_schema import CreatedTask, DetailedTask
from menu.celery.task import create_task_xlsx
from menu.services.service import Services, service_stub

xlsx_router = APIRouter(prefix="/create")


@xlsx_router.post(
    "/xlsx",
    tags=["xlsx"],
    description=CreateXLSLDocs.POST_XLSX,
    summary=CreateXLSLDocs.POST_XLSX,
    status_code=status.HTTP_202_ACCEPTED,
    response_model=CreatedTask,
)
async def create_task_and_xlsx(
    services: Services = Depends(service_stub),
):
    menus = await services.xlsx_service.get_all_data()
    task = create_task_xlsx.apply_async(args=[menus])

    return CreatedTask(task_id=task.id)


@xlsx_router.get(
    "/xlsx/{task_id}",
    tags=["xlsx"],
    description=CreateXLSLDocs.GET_XLSX,
    summary=CreateXLSLDocs.GET_XLSX,
    response_model=DetailedTask,
)
async def get_task_xlsx(
    task_id: str, services: Services = Depends(service_stub)
):

    task = services.tasks_service.get_task(task_id)

    return task
