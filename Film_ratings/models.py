from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models import signals

from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings

#By default, Django gives each model an auto-incrementing primary key

class Actor (models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname


class Director (models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname


class Film (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    created = models.DateTimeField('Date of Creation', auto_now_add=True)
    updated = models.DateTimeField('Date of Update', auto_now=True)
    #slug = models.SlugField(max_length = 200)
    
    
    @admin.display(description='Number of rates')    
    def count(self):
        rates = Rating.objects.filter(film = self) 
        return len(rates)  

    @admin.display(description='Average of rates')    
    def avg(self):
        rates = Rating.objects.values_list('rate',flat=True).filter(film=self)
        try:
            return round(sum(rates) /len(rates),2)
        except ZeroDivisionError:
            return 0
    
    def save(self, *args, **kwargs):
        self.url= slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.title
    
#@receiver(signals.pre_save, sender=Film)
#def populate_slug(sender, instance, **kwargs):
#    instance.slug = slugify(instance.title)

class Rating(models.Model):
    rate = models.IntegerField()
    film = models.ForeignKey(Film, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.film + ' ' + self.user + ' ' + self.rate
    
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)    