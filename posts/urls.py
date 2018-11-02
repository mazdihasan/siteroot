from django.urls import path
from posts import views

urlpatterns = [

path('', views.blog, name='blog'),
path('articles/<slug:title>/', views.article, name='article-detail'),

]
