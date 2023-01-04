from django.db import models


class TodoStatus(models.TextChoices):
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    status = models.CharField(
        max_length=50,
        choices=TodoStatus.choices,
        default=TodoStatus.todo,
    )