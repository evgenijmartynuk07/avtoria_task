from celery import Celery
from celery.schedules import crontab


app = Celery("car_parser.celeryconfig", broker="redis://redis:6379")
app.conf.update(
    include=["car_parser.tasks"],
    timezone="UTC"
)

app.conf.beat_schedule = {
    "start-collect-task": {
        "task": "car_parser.tasks.start_collect",
        "schedule":  crontab(minute="0", hour="12"),
    },
    "dump-db-task": {
        "task": "car_parser.tasks.dump_db",
        "schedule": crontab(minute="0", hour="0"),
    },
}
