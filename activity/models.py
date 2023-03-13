from django.db import models

# Create your models here.
class Activity(models.Model):
    activity_name = models.CharField(("activity_name"),max_length=50,unique=True)
    def __str__(self):
        return self.activity_name