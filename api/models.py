from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
# Create your models here.

class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, related_name="type")
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="form")
    option = models.JSONField(null=True, blank = True)
    optionResponse = models.JSONField(null=True, blank = True)
    text = models.TextField(null=True, blank = True)
    image = models.ImageField(null=True, blank = True)
    file = models.FileField(null=True, blank = True)
    url = models.URLField(null=True, blank = True)
    date = models.DateField(null=True, blank = True)
    time = models.TimeField(null=True, blank = True)
    datentime = models.DateTimeField(null=True, blank = True)
    email = models.EmailField(null=True, blank = True)
    def __str__(self) -> str:
        return self.title +" - " +str(self.form)

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    form = models.ForeignKey(Form, on_delete=models.DO_NOTHING, related_name="userform")
    time = models.DateTimeField(default=datetime.now)
    def __str__(self) -> str:
        return self.user
