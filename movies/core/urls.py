"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from core.views import get_all_movies, add_movie, view_movie, delete_movie, update_movie

urlpatterns = [
    url(r'^movies/', get_all_movies, name='get_all_movies'),
    url(r'^new-movie/', add_movie, name='add_movie'),
    url(r'^view-movie/(\d+)/', view_movie, name='view_movie'),
    url(r'^update-movie/(\d+)/', update_movie, name='update_movie'),
    url(r'^delete-movie/(\d+)/', delete_movie, name='delete_movie'),
]
