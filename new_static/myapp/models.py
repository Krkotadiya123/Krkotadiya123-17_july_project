from django.db import models

# Create your models here.

class top_tach(models.Model):
    crated=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


class notes(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=300)
    file=models.FileField(upload_to='MyNotes')

class contact_us(models.Model):
    uname=models.CharField(max_length=20)
    mail=models.EmailField()
    message=models.CharField(max_length=200)