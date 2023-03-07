from django.db import models
from activity.models import Activity
from user.models import User


# Create your models here.

    
class Feed(models.Model):
    feed_id = models.AutoField(('feed_id'),primary_key=True,)
    user_id = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, db_column="user_id",)
    feed_activity = models.ForeignKey(Activity, related_name="activity", on_delete=models.CASCADE, db_column="activity_name")
    photos = models.ImageField(("photos"), upload_to="feed/images",blank=True, height_field=None, width_field=None, max_length=None)
    location = models.CharField(("location"), max_length=50)
    time = models.DateTimeField(("time"), auto_now=False, auto_now_add=True)
    content = models.TextField(("content"))
    views = models.IntegerField(("views"),auto_created=0)
    location_name = models.CharField(("location name"), max_length=50)

    def __int__(self):
        return self.feed_id

