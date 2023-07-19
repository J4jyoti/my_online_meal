from django.db import models

# Create your models here.: define your database
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateTimeField()
    
# name shown in database rater than contact object
def _str_(self):
    return self.name
