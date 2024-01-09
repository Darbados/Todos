import datetime

from django.utils import timezone


TZ = timezone.get_default_timezone()


def todo_localize(dt: timezone.datetime) -> datetime.datetime:
    return datetime.datetime.astimezone(dt, TZ)
