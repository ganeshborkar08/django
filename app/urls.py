from django.urls import path, include

from .views import *

urlpatterns = [
    path('welcome/', WelcomeView.as_view(), name='api-welcome'),
]