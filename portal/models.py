from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Questions(models.Model):
    Name = models.CharField(max_length=50,default='--')
    Deptartment = models.CharField(max_length=50,default='--')
    contact_num = models.CharField(max_length=50,default='--')
    now = timezone.now()
    Q1 = models.TextField(default='--')
    Q2 = models.TextField(default='--')
    Q3 = models.TextField(default='--')
    Q4 = models.TextField(default='--')
    Q5 = models.TextField(default='--')
    Q6 = models.TextField(default='--')
    Q7 = models.TextField(default='--')
    Q8 = models.TextField(default='--')
    Q9 = models.TextField(default='--')
    Q10 = models.TextField(default='--')

    def __str__(self):
        return self.Name
