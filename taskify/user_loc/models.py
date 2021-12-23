from django.db import models
from django.db.models import JSONField
# from django.contrib.gis.db import models as modo

# Create your models here.
class mfy_task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    task_description = models.CharField(max_length=1000)


class mfy_users(models.Model):
    user_phone_no = models.IntegerField(primary_key=True)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    task_id = models.ForeignKey(mfy_task, on_delete=models.DO_NOTHING)
    distance = models.FloatField(max_length=25, null=True)
    # location = modo.PointField()


class mapping_table(models.Model):
    user_phone = models.IntegerField(primary_key=True)
    task_to_distance = JSONField()


