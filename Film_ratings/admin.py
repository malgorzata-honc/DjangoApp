from django.contrib import admin
from .models import Actor, Director, Film, Rating



class ActorAdmin (admin.ModelAdmin):
    fields = [
        'name', 
        'surname',
        ]
    list_display = ('id', 'name', 'surname')

class DirectorAdmin (admin.ModelAdmin):
    fields = [
        'name', 
        'surname',
        ]
    list_display = ('id', 'name', 'surname')   

class FilmAdmin (admin.ModelAdmin):
       
    fields = [
        'title',
        #'slug'
        'description',
        'director', 
        'actors', 
        'updated', 
        ]    
    list_display = ('title', 'count', 'avg',)

class RatingAdmin (admin.ModelAdmin):
    fields = [
        'rate', 
        'film',
        'user',
        ]
    list_display = ( 'rate','film', 'user')



admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Rating, RatingAdmin)