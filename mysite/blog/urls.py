from django.urls import path
from . import views
from django.conf.urls import include, url
urlpatterns = [
    path('', views.post_list, name='post_list'),
]