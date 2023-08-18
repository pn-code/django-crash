from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guest', views.guest, name='guest'),
    path("<str:name>", views.greet, name="greet")
]