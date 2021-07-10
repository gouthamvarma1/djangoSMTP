from django.db import models

# Create your models here.

class students(models.Model):
    email=models.CharField(max_length=100)
    status=models.IntegerField()

    def __str__(self):
        return self.email