from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='picture')
    description = models.TextField()

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='picture')
    qualification = models.CharField(max_length=250)
    position = models.TextField()

    def __str__(self):
        return self.name
