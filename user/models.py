
from django.utils import timezone
from django.db import models

# Create your models here.
class User(models.Model):
    GENDERS = (
        ('M', '남성'),
        ('W', '여성'),
    )
    name = models.CharField(('username'), max_length=20, unique=True,default='')
    user_id = models.CharField(('user id'), max_length=32, unique=True,)
    user_password = models.CharField(('user password'), max_length=128)
    nickname = models.CharField(('nickname'), max_length=20, unique=True)
    is_staff = models.BooleanField(('staff status'), default=False)
    information = models.TextField(('information'), max_length=200, blank=True)
    profile_image = models.ImageField()
    like_places = models.TextField((""))
    like_activities = models.TextField((""))
    bookmark_list = models.TextField((""))
    date_birthday = models.DateField(('date birthday'), null=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)
    country = models.CharField(("country"), max_length=50)
    phone_number = models.CharField(("phone_number"), max_length=20)
    def __str__(self):
        return self.name
class Follow(models.Model):
    from_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='to_user')
    to_user   = models.ForeignKey('User', on_delete=models.CASCADE, related_name='from_user')
    