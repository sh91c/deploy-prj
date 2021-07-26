from django.urls import path
from . import views

urlpatterns = [
    path('get/sync_to_async_view', views.sync_to_async_view),
    path('get/sync_view', views.sync_view),
]