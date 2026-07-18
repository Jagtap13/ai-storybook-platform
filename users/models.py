from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    ROLE_CHOICES = (
        ('student','Student'),
        ('parent','Parent/Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    age = models.PositiveBigIntegerField(null=True,blank=True)
    learning_level = models.CharField(max_length=20,blank=True)
    favourite_topics = models.JSONField(default=list,blank=True)

    def __str__(self):
        return f"{self.user.username}({self.role})"
    