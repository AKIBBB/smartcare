from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=25)
    deccription=models.TextField()
    image=models.ImageField(upload_to="service/images/")