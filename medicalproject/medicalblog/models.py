from django.db import models

# Create your models here.
class Post(models.Model):
    People=models.CharField(max_length=255)
    Doctor=models.CharField(max_length=255)
    Bio=models.CharField(max_length=255)
    Address=models.CharField(max_length=255)
    Product=models.CharField(max_length=255)