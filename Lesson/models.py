from django.db import models
from UserManager.models import UserAccount

class Level(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    number = models.IntegerField(unique=True)

class Questions(models.Model):
    id = models.IntegerField(primary_key=True)
    level_number = models.IntegerField()
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

class AssignLevels(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    Level = models.ForeignKey(Level, on_delete=models.CASCADE)