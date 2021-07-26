from django.urls import path
from . import views

urlpatterns = [
    path('get/async-view', views.sync_to_async_view),
    path('get/sync-view', views.sync_view),
]