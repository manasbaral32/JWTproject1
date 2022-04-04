from django.db import models
from django.urls import reverse
# Create your models here.

# this is for testing purpose

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=50)
    salary = models.IntegerField()
    address = models.CharField(max_length=50)
    mobile = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse("employees")
