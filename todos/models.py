from django.conf import settings
from django.db import models


class Todo(models.Model):
    class TodoStatus(models.IntegerChoices):
        NOT_STARTED = 1
        ACTIVE = 2
        COMPLETED = 3

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(choices=TodoStatus.choices, default=TodoStatus.NOT_STARTED)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
