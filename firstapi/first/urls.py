from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('article_list', views.article_list),
    path('detail/<int:pk>', views.article_detail),
    #path('article_list', views.article_list),
    #path('article_list', views.article_list),
]
