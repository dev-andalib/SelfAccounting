from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('accountant', 'Accountant'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='accountant')

    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username