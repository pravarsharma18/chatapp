from django.urls import path
from .views import HomePage


urlpatterns = [
    path("g/<str:group_name>/", HomePage.as_view())
]
