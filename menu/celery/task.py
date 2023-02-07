import uuid

import xlsxwriter

from menu.services.db_fill.db_models import Menus

from .celery_app import celery


@celery.task(name="menu.create_task_xlsx:celery")
def create_task_xlsx(menus_list: list[dict]):
    task = f"task_data/{uuid.uuid4().hex}.xlsx"
    generate_xlsx(task, menus_list)

    return task


def generate_xlsx(task: str, menus: list[dict]):
    with xlsxwriter.Workbook(task) as book:
        book_sheet = book.add_worksheet("Menu")
        column = 0
        row = 0

        for i, menu in enumerate(menus):
            menu = Menus(**menu)

            book_sheet.write(row, column, menu.title)
            book_sheet.write(row, column + 1, menu.description)

            column += 2
            row += 1

            for submenu in menu.submenus:
                book_sheet.write(row, column, submenu.title)
                book_sheet.write(row, column + 1, submenu.description)

                row += 1
                column += 2

                for dish in submenu.dishes:
                    book_sheet.write(row, column, dish.title)
                    book_sheet.write(row, column + 1, dish.description)
                    book_sheet.write(row, column + 2, dish.price)

                    row += 1

                column -= 2

            column = 0
            row += 2
