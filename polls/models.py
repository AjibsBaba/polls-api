from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices',
                             on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=100)

    def __str__(self):
        return self.choiceText


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("poll", "voter")
