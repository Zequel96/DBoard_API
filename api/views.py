from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Game
from .serializers import GameSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getAllGames(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGame(request, gameTitle):
    game = Game.objects.get(pk=gameTitle)
    if game is not None:
        return render(request, 'testing.html', {'game':game})
    return Response('Not Found')

@api_view(['POST'])
def addGame(request):
    if request.method == 'POST':
        serializer = GameSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
