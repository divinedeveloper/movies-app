from django.db import models
from django.utils import timezone

# Create your models here.

class Movie(models.Model):
	name = models.CharField(blank = False, max_length = 50)
	date_created = models.DateTimeField(default=timezone.now)

class Location(models.Model):
	name = models.CharField(blank = False, max_length = 50)
	movie = models.ForeignKey(Movie)

class Timing(models.Model):
	time = models.DateTimeField(blank = False)
	location = models.ForeignKey(Location)
