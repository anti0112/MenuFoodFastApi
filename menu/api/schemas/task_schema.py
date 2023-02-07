from pydantic import BaseModel


class CreatedTask(BaseModel):
    task_id: str


class DetailedTask(CreatedTask):
    status: str
    result: str
