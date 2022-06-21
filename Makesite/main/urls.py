from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('proflie/', views.proflie, name="proflie"),
    path('work/', views.work, name="work"),
    path('like/', views.like, name="like"),
    path('sns/', views.sns, name="sns"),

]
