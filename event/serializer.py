import json

from django.contrib.auth import authenticate
from rest_framework import serializers
# pip install Django django-rest-framework
from .models import Event as event
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    # event_id = serializers.SerializerMethodField(method_name='get_event_id')

    class Meta:
        model = event
        # read_only_fields = ('user')
        fields = '__all__'
        read_only_field = ['_id', 'user']

    # def get_event_id(self, obj):
        # event = obj.event_id
        # latest = event.objects.filter(event_id__gt=1).last()
        # last_id = latest.event_id
        # event_id2 = last_id+1
        # return last_id

    def get_user(self, obj):
        pass

    # def create(self, validated_data):
    #     return event.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     event.objects.filter(event_id=instance.event_id).update(**validated_data)
    #
    # def remove(self):
    #     pass

# class UserSerializer(serializers.ModelSerializer):

