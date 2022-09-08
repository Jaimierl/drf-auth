from django.contrib.auth import get_user_model
from django.db import models


class ToDo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    thing_to_do = models.CharField(max_length=64)
    task_description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.thing_to_do