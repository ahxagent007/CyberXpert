from django.db import models
from UserManager.models import UserAccount

class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    number = models.IntegerField(unique=True)

    def __str__(self):
        return '[{0}] {1}'.format(self.number, self.name)

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    level_number = models.IntegerField()
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

class AssignLevels(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    Level = models.ForeignKey(Level, on_delete=models.CASCADE)


class QuizPaper(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    user_score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    total_answered = models.IntegerField(default=0)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    answer_no = models.IntegerField(default=0)