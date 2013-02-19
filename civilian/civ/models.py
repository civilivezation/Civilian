from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

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

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = []

class FactionForm(forms.ModelForm):
    class Meta:
        model = Faction
        fields = []

class UsersForm(form.ModelForm):
    class Meta:
        model = Users
        fields =[]
