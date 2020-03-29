from django.urls import path
from device.views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
]
