from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    submission_date = models.DateTimeField()
    full_body = models.TextField()
    
