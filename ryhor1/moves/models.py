from django.db import models

# Create your models here.
class locations(models.Model):
    name = models.CharField(max_length=30)
    locs = models.ManyToManyField('self',symmetrical=True)
    
class entity(models.Model):
    name = models.CharField(max_length=30,unique=True)
    type = models.CharField(max_length=30)
    location = models.ForeignKey(locations,related_name="entity")
    
