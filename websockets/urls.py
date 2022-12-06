from django.urls import path
from .views import homepage

urlpatterns = [
    path("group/<str:group_name>/", homepage)
]