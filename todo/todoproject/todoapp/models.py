from datetime import timezone
from datetime import datetime

from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=255)
    priority=models.IntegerField()
   # date=models.DateField()
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name