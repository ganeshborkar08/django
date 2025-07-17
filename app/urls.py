from django.urls import path

from .views import *

urlpatterns = [
    path('welcome/', WelcomeView.as_view(), name='api-welcome'),
]