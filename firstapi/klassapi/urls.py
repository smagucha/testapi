from django.urls import path
from .views import(
 ArticleAPIView,
 MyView,
 ArticleDetails,
ArtistList,
ArtistDetail,
ArtistDelete,
ArtistUpdate
       )

urlpatterns = [
    path('homeofclass/', MyView.as_view()),
    path('articlelist', ArticleAPIView.as_view()),
    path('genericlist', ArtistList.as_view()),
    path('classdetail/<int:id>', ArticleDetails.as_view()),
    path('<int:pk>/classdetail',ArtistDetail.as_view()),
    path('<int:pk>/classdelete',ArtistDelete.as_view()),
    path('<int:pk>/classupdate',ArtistUpdate.as_view()),



]
