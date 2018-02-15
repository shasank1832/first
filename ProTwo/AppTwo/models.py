from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264,unique=False)
    last_name = models.CharField(max_length=264,unique=False)
    email= models.EmailField(max_length=264)


    def __str__(self):
        return self.email
