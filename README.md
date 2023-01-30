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
#### 2. Для запуска API напишите эту команду
```
docker-compose -f docker-compose.yml up -d
```
#### 3. Для запуска тестов напишите команду
```
docker-compose -f docker-compose.test.yml up -d
```
___
