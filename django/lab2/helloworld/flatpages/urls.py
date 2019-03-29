from django.urls import path
from flatpages import views

urlpatterns = [
    path('', views.home, name='home'),
]