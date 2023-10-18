from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# class Poll(models.Model):
#     poll_name = models.CharField('poll name',max_length=45)
#     created_at = models.DateTimeField('date created',auto_created=True)
#     updated_at =models.DateTimeField('last updated')

# class User(models.Model):
#     user_name = models.CharField('user name',max_length=255)
#     user_email = models.CharField('user email',max_length = 255)
#     created_at = models.DateTimeField('date created',auto_created= True)
#     updated_at = models.DateTimeField('last updated')

# class Vote(models.Model):
#     vote= models.CharField('vote',max_length=255)
#     created_at = models.DateTimeField('date created',auto_created=True)
#     updated_at = models.DateTimeField('last updated')


class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)