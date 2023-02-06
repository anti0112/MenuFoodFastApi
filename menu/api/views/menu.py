from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from menu.api.docs.documentation import MenuDocs
from menu.api.schemas.menu_schema import MenuIn, MenuOut
from menu.services.service import Services, service_stub

router = APIRouter(prefix="/menus")


@router.get(
    "/",
    tags=["Menu"],
    description=MenuDocs.GET_LIST,
    summary=MenuDocs.GET_LIST,
    response_model=list[MenuOut],
)
async def get_menus(services: Services = Depends(service_stub)):
    all_menus = await services.menu_service.get_list()

    return all_menus


@router.post(
    "/",
    tags=["Menu"],
    description=MenuDocs.POST_CREATE,
    summary=MenuDocs.POST_CREATE,
    response_model=MenuOut,
    status_code=201,
)
async def create_menu(
    menu: MenuIn, services: Services = Depends(service_stub)
):
    menu = await services.menu_service.create(
        title=menu.title, description=menu.description
    )

    return menu


@router.get(
    "/{menu_id}",
    tags=["Menu"],
    description=MenuDocs.GET_DETAIL,
    summary=MenuDocs.GET_DETAIL,
    response_model=MenuOut,
)
async def get_menu_information(
    menu_id: int, services: Services = Depends(service_stub)
):
    menu = await services.menu_service.get_detail(menu_id=menu_id)

    return menu


@router.patch(
    "/{menu_id}",
    tags=["Menu"],
    description=MenuDocs.PATCH_UPDATE,
    summary=MenuDocs.PATCH_UPDATE,
    response_model=MenuOut,
)
async def update_menu_information(
    menu_id: int, menu: MenuIn, services: Services = Depends(service_stub)
):
    menu = await services.menu_service.update(
        menu_id, title=menu.title, description=menu.description
    )

    return menu


@router.delete(
    "/{menu_id}",
    tags=["Menu"],
    description=MenuDocs.DELETE,
    summary=MenuDocs.DELETE,
)
async def delete_menu(
    menu_id: int, services: Services = Depends(service_stub)
):
    menu = await services.menu_service.delete(menu_id)

    return JSONResponse(
        content={"status": menu, "message": "The menu has been deleted"}
    )
