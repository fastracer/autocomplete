from django.db import models

# Create your models here.
class Bio(models.Model):
    test = models.CharField(max_length=255)


class Location(models.Model):
    place = models.CharField(max_length=255)


class PreviousClient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Skill(models.Model):
    title = models.CharField(max_length=255)

