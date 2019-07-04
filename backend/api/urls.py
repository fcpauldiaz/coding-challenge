# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('tweet/', views.TweetList.as_view()),
    path('tweet/<int:pk>/', views.TweetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)