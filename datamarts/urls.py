from django.urls import path

from datamarts.views import health

urlpatterns = [
    path("health/", health, name="health"),
]
