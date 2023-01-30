from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from menu.api.docs.documentation import SubmenuDocs
from menu.api.schemas.submenu_schema import SubmenuOut
from menu.api.schemas.menu_schema import MenuIn
from menu.services.service import Services, service_stub

router = APIRouter(prefix="/menus/{menu_id}/submenus")


@router.get("/", tags=["Submenu"], description=SubmenuDocs.GET_LIST,
            summary=SubmenuDocs.GET_LIST, response_model=list[SubmenuOut]
            )
async def get_all_submenus(menu_id: int, services: Services = Depends(service_stub)):
    submenus = await services.submenu_service.get_list(menu_id=menu_id)

    return submenus


@router.get("/{submenu_id}", tags=["Submenu"], description=SubmenuDocs.GET_DETAIL,
            summary=SubmenuDocs.GET_DETAIL, response_model=SubmenuOut
            )
async def get_submenu_information(submenu_id: int, services: Services = Depends(service_stub)):
    submenu = await services.submenu_service.get_detail(submenu_id=submenu_id)

    return submenu


@router.post("/", tags=["Submenu"], description=SubmenuDocs.POST_CREATE,
             summary=SubmenuDocs.POST_CREATE, response_model=SubmenuOut, status_code=201
             )
async def create_submenu(menu_id: int, submenu: MenuIn, services: Services = Depends(service_stub)):
    submenu = await services.submenu_service.create(
        menu_id=menu_id,
        title=submenu.title,
        description=submenu.description
    )

    return submenu


@router.patch("/{submenu_id}", tags=["Submenu"], description=SubmenuDocs.PATCH_UPDATE,
              summary=SubmenuDocs.PATCH_UPDATE, response_model=SubmenuOut
              )
async def update_submenu_information(
        submenu_id: int,
        submenu: MenuIn, services: Services = Depends(service_stub)
):
    submenu = await services.submenu_service.update(submenu_id, title=submenu.title, description=submenu.description)

    return submenu


@router.delete("/{submenu_id}", tags=["Submenu"], description=SubmenuDocs.DELETE,
               summary=SubmenuDocs.DELETE
               )
async def delete_submenu(submenu_id: int, services: Services = Depends(service_stub)):
    menu = await services.submenu_service.delete(submenu_id=submenu_id)

    return JSONResponse(content={"status": menu, "message": "The submenu has been deleted"})
