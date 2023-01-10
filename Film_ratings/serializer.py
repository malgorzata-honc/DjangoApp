from .models import Actor, Director, Film, Rating
from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import Account 

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Actor
        fields = [ 'id', 'name', 'surname']


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Director
        fields = [ 'id', 'name', 'surname']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'directors', 'actors', 'created', 'updated' ]

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class RatingSerializer (serializers.HyperlinkedModelSerializer):
    film = FilmSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Rating
        fields = ['rate', 'film', 'user']       

