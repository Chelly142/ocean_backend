from django.db import models
from user.models import User

# Create your models here.
class Feed(models.Model):
    name = models.CharField(('feedname'), max_length=20, unique=True,default='')
    feed_id = models.CharField(("feed id"), max_length=50)
    user_id = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, db_column="user_id")
    photos = models.ImageField(("photos"), upload_to=None, height_field=None, width_field=None, max_length=None)
    location = models.CharField(("location"), max_length=50)
    time = models.DateTimeField(("time"), auto_now=False, auto_now_add=True)
    content = models.TextField(("content"))
    views = models.IntegerField(("views"))
    category = models.CharField(("category"), max_length=50)
    location_name = models.CharField(("location name"), max_length=50)

    def __str__(self):
        return self.name