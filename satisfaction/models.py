from djongo import models;
from event.models import User


class Satisfaction(models.Model):
    use_in_migrations = True
    _id = models.ObjectIdField()
    satisfaction_id = models.IntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=30,blank=True)
    result = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f'[{self.pk}] \n {self.user} \n {self.created} \n {self.type}\n' \
               f'{self.result} 등 입력 완료'

    class Meta:
        db_table = 'satisfaction'

