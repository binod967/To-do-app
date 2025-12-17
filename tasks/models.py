from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    priority_choices = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, blank=True)
    priority = models.CharField(max_length=10, choices=priority_choices, default='Medium')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

   