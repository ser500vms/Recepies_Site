from django.urls import path
from .views import (
    HomeView,
    RegistrationView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('reg/', RegistrationView.as_view(), name='registration_page'),
]