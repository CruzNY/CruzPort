from django.db import models
# Create your models here.

#Creating Objects for our database
class project(models.Model):
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=80)
    submission_date = models.DateTimeField() 
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    full_body = models.TextField()
    
