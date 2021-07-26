from django.urls import path
from . import views

urlpatterns = [
    path('get/test', views.test_view),
]