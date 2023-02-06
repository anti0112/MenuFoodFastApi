from celery import Celery
from menu.core.config import C_BROKER_URL, C_RESULT_BACKEND


def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        _, queue = name.split(":")
        return {"queue": queue}

    return {"queue": "celery"}


celery = Celery(
    __name__,
    include=["menu.celery.task"],
    backend=C_RESULT_BACKEND,
    broker=C_BROKER_URL
)


celery.conf.task_default_queue = "celery"
celery.conf.task_routes = (route_task,)
celery.autodiscover_tasks()
