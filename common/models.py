from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES=[
        ('admin', 'Admin'),
        ('placement_admin', 'Placement Admin'),
        ('placement_team', 'Placement Team'),
        ('tutors', 'Tutors'),
        ('students', 'Students')
    ]

    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        default='admin',
    )