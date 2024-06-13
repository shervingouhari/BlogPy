from django.urls import path
from . import views
from . import API


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('articles/', API.ArticleAPI.as_view()),
    path('articles/<int:article_id>/', API.ArticleAPI.as_view()),
]
