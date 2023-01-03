from django.urls import path
from blog import views

urlpatterns = [
    path('', views.base),
    path('home', views.home),
    path('blogs/<slug:url>', views.posts),
    path('cats/<slug:url>', views.cats),
]