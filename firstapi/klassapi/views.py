from django.views import View
from . import views
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework .decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

class MyView(View):
    def get(self, request):
        return HttpResponse('home of class based views')

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDelete(generics.DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistUpdate(generics.UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArticleAPIView(APIView):
    def get(self, request):
        articles = Artist.objects.all()
        serializer = ArtistSerializer(articles, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):

    def get_object(self,id):
        try:
            return  Artist.objects.get(id = id)
        except Artist.DoesNotExist:
            return HttpResponse(status =status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        artist=self.get_object(id)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def put(self,request, id):
        artist=self.get_object(id)
        serializer = ArtistSerializer(artist, data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        artist=self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
