from django.db import models
from django.core.mail.message import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404


class CustomMessage(models.Model):
    message_text = models.CharField(max_length=10000)
    message_from = models.CharField(max_length=100)
    message_to = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    subject_text = models.CharField(max_length=200)
    is_viewed = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return "message = " + str(self.message_text) + "\nfrom = " + str(self.message_from) + " \nto = " + str(self.message_to) + " \nsubject = " + str(
            self.subject_text) + "\n"


class InMessage(models.Model):
    mail = models.ForeignKey(CustomMessage, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def getmail(self):
        return get_object_or_404(CustomMessage, mail_id=self.mail.id)

    def getuser(self):
        return self.user


class OutMessage(models.Model):
    mail = models.ForeignKey(CustomMessage, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
