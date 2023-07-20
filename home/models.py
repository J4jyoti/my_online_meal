from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12, null=True, unique=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name # we get name instead of contact obj1
