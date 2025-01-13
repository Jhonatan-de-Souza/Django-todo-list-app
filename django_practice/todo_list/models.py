from django.db import models

class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=50,null=False,blank=False)
    description = models.TextField(max_length=300,blank=True)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)