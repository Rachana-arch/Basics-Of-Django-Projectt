from django.db import models


# Create your models here.
class mfy_task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    task_description = models.CharField(max_length=1000)


class mfy_users(models.Model):
    user_phone_no = models.IntegerField(primary_key=True)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    task_id = models.ForeignKey(mfy_task, on_delete=models.DO_NOTHING)