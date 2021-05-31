from django.contrib import admin
from django.urls import path
from .apis import api


urlpatterns = [
    path("", api.urls),
]
