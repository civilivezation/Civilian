from django.db import models

class Faction(models.Model):
    name = models.CharField(max_length=60,unique=True)
    members = models.IntegerField()

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=35,unique=True)
    fact = models.ForeignKey(Faction)
    money = models.IntegerField()
    city = models.OneToOneField(City)

    def __unicode__(self):
        return self.name
