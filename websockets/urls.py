from django.urls import path
from .views import homepage

urlpatterns = [
    path("<str:group_name>/", homepage)
]