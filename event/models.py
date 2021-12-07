from datetime import datetime
from djongo import models


class User(models.Model):
    # _id = models.ObjectIdField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class Event(models.Model):
    use_in_migrations = True
    _id = models.ObjectIdField()
    event_id = models.IntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    classification = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    title = models.CharField(max_length=50, blank=True)
    start = models.CharField(max_length=25,  blank=True)
    end = models.CharField(max_length=25,  blank=True)
    location = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title



    class Meta:
        db_table = 'events'

