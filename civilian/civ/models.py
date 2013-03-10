from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class Faction(models.Model):
    name = models.CharField(max_length=60,unique=True)
    members = models.IntegerField()
    score = models.IntegerField()
    food = models.IntegerField()
    art = models.IntegerField()
    military = models.IntegerField()
    science = models.IntegerField()
    colour = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    money = models.IntegerField() 
    totalpopulation = models.IntegerField()
    workingpopulation = models.IntegerField()
    nonworkingpopulation = models.IntegerField()
    farms = models.IntegerField()
    labs = models.IntegerField()
    barracks = models.IntegerField()
    studios = models.IntegerField()

    def __unicode__(self):
        return self.name

class Building(models.Model):
    buildtype = models.CharField(max_length=50)
    cost = models.IntegerField()
    profit = models.IntegerField()
    residents = models.IntegerField()
    workers = models.IntegerField()
    pfood = models.IntegerField()
    part = models.IntegerField()
    pmilitary = models.IntegerField()
    pscience = models.IntegerField()
    
    def __unicode__(self):
        return self.buildtype

class Character(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    cost = models.IntegerField()
    money = models.FloatField()
    food = models.FloatField()
    science = models.FloatField()
    military = models.FloatField()
    arts = models.FloatField()
    
    def __unicode__(self):
        return self.name

class Users(models.Model):
    user = models.OneToOneField(User)
    fact = models.ForeignKey(Faction)
    city = models.OneToOneField(City)
    character = models.ForeignKey(Character)

    def __unicode__(self):
        return self.user.username

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
        widgets = {
            'password':forms.PasswordInput(),
            }
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = []

class FactionForm(forms.ModelForm):
    class Meta:
        model = Faction
        fields = []

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields =[]
