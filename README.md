## Проект для YLab

___
### Стек:
- python 3.11
- FastApi 0.89.1
- PostgreSQL 14.3
___
### Для запуска проекта на локальной машине следует выполнить следующие действия:

#### 1. Создать  файл `.env` и записать в него переменные окружения из `.env.example`
```
cp .env.example .env
```
#### 2. Для запуска напишите эту команду
```
docker compose -f docker-compose.yml -f docker-compose.test.yml up -d
```
#### Если контейнеры выдали ошибку выполните команду `docker compose up -d` повторно
___


