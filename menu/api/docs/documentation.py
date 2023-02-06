class MenuDocs:
    GET_DETAIL = "Получить меню"
    GET_LIST = "Получить все меню"
    POST_CREATE = "Создать новое меню"
    PATCH_UPDATE = "Обновить меню"
    DELETE = "Удалить меню, и связанные с ним подменю и блюда"


class SubmenuDocs:
    GET_DETAIL = "Получить подменю"
    GET_LIST = "Получить все подменю определенного меню"
    POST_CREATE = "Создать подменю"
    PATCH_UPDATE = "Обновить подменю"
    DELETE = "Удалить подменю и блюда связанные с ним"


class DishDocs:
    GET_DETAIL = "Получить блюдо"
    GET_LIST = "Получить все блюда"
    POST_CREATE = "Создать блюдо"
    PATCH_UPDATE = "Обновить блюдо"
    DELETE = "Удалить блюдо"


class StuffDocs:
    POST_STUFF = "Заполнить базу тестовыми данными"


class CreateXLSLDocs:
    POST_XLSX = "Создать задачу создания xlsx файла"
    GET_XLSX = "Получить информацию о задаче"
