from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import  get_user_model

# Create your models here.

class Math(models.Model):
    oper = models.CharField(max_length=1)
    l1 = models.IntegerField()
    l2 = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    def __str__(self):
        return f"Math operation: {self.oper}, arguments: {self.l1}, {self.l2}"