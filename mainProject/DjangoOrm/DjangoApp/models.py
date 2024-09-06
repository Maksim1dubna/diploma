from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name