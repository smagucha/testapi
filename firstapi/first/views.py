from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer

def home(request):
    return HttpResponse('this is home')

def article_list(request):

    if request.method =='GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data =JSONparser().parse(request)
        serializer = ArticleSerializer(data= data)

        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
