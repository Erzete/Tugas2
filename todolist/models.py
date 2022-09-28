from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
class Task(models.Model):
	user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
	date = models.DateField(default=timezone.now)
	title = models.CharField(max_length=50)
	description = models.TextField()