from django.http import JsonResponse
from django.views import View

class WelcomeView(View):
    def get(self, request):
        return JsonResponse({"message": "Welcome to the API!"})