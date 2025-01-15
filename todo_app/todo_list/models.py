from django.db import models


class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
