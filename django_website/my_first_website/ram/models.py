from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pokemon(models.Model):
    Pokemon_Name = models.CharField(max_length=300)
    POWER = models.IntegerField()
    value = models.IntegerField()
    class Meta:
        db_table = "Pokemons"




class UserInfo(models.Model):
    UserInfo = models.OneToOneField(User,on_delete=models.PROTECT)
    def __str__(self):
        return self.UserInfo.username
