from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from menu.api.docs.menu_methods_description import DishApiDocs
from menu.api.schemas.dish_schema import DishOut, DishIn
from menu.services.service import service_stub, Services

router = APIRouter(prefix="/menus/{menu_id}/submenus/{submenu_id}/dishes")


@router.get(
    "/",
    tags=["Dish"], description=DishApiDocs.GET_LIST, summary=DishApiDocs.GET_LIST,
    response_model=list[DishOut]
)
async def get_dishes(services: Services = Depends(service_stub)):
    dishes = await services.dishes_service.get_list()

    return dishes


@router.get(
    "/{dish_id}",
    tags=["Dish"], description=DishApiDocs.GET_DETAIL, summary=DishApiDocs.GET_DETAIL,
    response_model=DishOut
)
async def get_dish_information(dish_id: int, services: Services = Depends(service_stub)):
    dish = await services.dishes_service.get_detail(dish_id=dish_id)

    return dish


@router.post(
    "/",
    tags=["Dish"], description=DishApiDocs.POST_CREATE, summary=DishApiDocs.POST_CREATE,
    response_model=DishOut, status_code=201
)
async def create_dish(submenu_id: int, dish: DishIn, services: Services = Depends(service_stub)):
    dish = await services.dishes_service.create(submenu_id, dish.title, dish.description, dish.price)

    return dish


@router.patch(
    "/{dish_id}",
    tags=["Dish"], description=DishApiDocs.PATCH_UPDATE, summary=DishApiDocs.PATCH_UPDATE,
    response_model=DishOut
)
async def update_dish(dish_id: int, dish: DishIn, services: Services = Depends(service_stub)):
    dish = await services.dishes_service.update(
        dish_id, title=dish.title, description=dish.description, price=dish.price
    )

    return dish


@router.delete("/{dish_id}", tags=["Dish"], description=DishApiDocs.DELETE, summary=DishApiDocs.DELETE)
async def delete_dish(dish_id: int, services: Services = Depends(service_stub)):
    dish = await services.dishes_service.delete(dish_id)

    return JSONResponse(content={"status": dish, "message": "The dish has been deleted"})
