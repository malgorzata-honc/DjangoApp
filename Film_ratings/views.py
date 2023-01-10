from rest_framework import viewsets
from .serializer import ActorSerializer, DirectorSerializer, FilmSerializer, RatingSerializer
from .models import Actor, Director, Film, Rating

from rest_framework.response import Response
from rest_framework import status as st


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def create(self, request, *args, **kwargs):
        try:
            name = request.data.get('name')
            surname = request.data.get('surname')
            actor = Actor.objects.create(name=name, surname=surname)
            serializer = ActorSerializer(actor, many=False)
            response = {'message': 'Actor successfully created', 'result': serializer.data}
            return Response(response,status=st.HTTP_201_CREATED)
        except:
            response = {'message': 'Something wrong or actor didnt exists ! '}
            return Response(response, status=st.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            actor_object = Actor.objects.get(id=pk)
            actor_object.name = request.data.get('name')
            actor_object.surname = request.data.get('surname')
            actor_object.save()
            serializer = ActorSerializer(actor_object, many=False)
            response = {'message': 'Actor successfully updated ', 'result': serializer.data}
            return Response(response,status=st.HTTP_201_CREATED)
        except:
            response = {'message': 'Something wrong or actor didnt exists ! '}
            return Response(response, status=st.HTTP_400_BAD_REQUEST)        
   
class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        try:
            name = request.data.get('name')
            surname = request.data.get('surname')
            director = Director.objects.create(name=name, surname=surname)
            serializer = DirectorSerializer(director, many=False)
            response = {'message': 'Director successfully created', 'result': serializer.data}
            return Response(response,status=st.HTTP_201_CREATED)
        except:
            response = {'message': 'Something wrong or director didnt exists ! '}
            return Response(response, status=st.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            director_object = Director.objects.get(id=pk)
            director_object.name = request.data.get('name')
            director_object.surname = request.data.get('surname')
            director_object.save()
            serializer = DirectorSerializer(director_object, many=False)
            response = {'message': 'Director successfully updated ', 'result': serializer.data}
            return Response(response,status=st.HTTP_201_CREATED)
        except:
            response = {'message': 'Something wrong or director didnt exists ! '}
            return Response(response, status=st.HTTP_400_BAD_REQUEST)

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def create(self, request):
        try:
            actors_data = request.data.pop('actor')         
            actor, created = Actor.objects.get_or_create(name=actors_data['name'], surname=actors_data['surname'])
            title = request.data.get('title')
            description = request.data.get('description')
            director = request.data.get('directors')  
            film = Film.objects.create(title=title, actor=actor, description=description, director=director, created=created, updated=updated)
            serializer = FilmSerializer(film, many=False)
            response = {'message': 'Film successfully created', 'result': serializer.data}
            return Response(response, status=st.HTTP_201_CREATED)

        except:
            response = {'message': 'Something wrong or film with the same title exists ! Check your data... '}
            return Response(response, status=st.HTTP_400_BAD_REQUEST)                



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def create(self, request):
        try:         
            film = request.data.get('film') 
            rate = request.data.get('rate')      
            rating = Rating.objects.create(film=film, rate=rate)
            serializer = RatingSerializer(rating, many=False)
            response = {'message': 'Rating successfully created', 'result': serializer.data}
            return Response(response, status=st.HTTP_201_CREATED)

        except:
            response = {'message': 'Something wrong or rating with the same parameters exists ! Check your data... '}
            return Response(response, status=st.HTTP_400_BAD_REQUEST)   

