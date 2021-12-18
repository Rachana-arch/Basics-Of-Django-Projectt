# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import mfy_users


# Create a model serializer
class UsersSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = mfy_users
        # fields = ('user_phone_no', 'latitude', 'longitude', 'task_id')
        fields = ("__all__")

    def update(self, instance, validated_data):
        instance.user_phone_no = validated_data.get('user_phone_no', instance.user_phone_no)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.task_id = validated_data.get('task_id', instance.task_id)
        instance.save()
        return instance
