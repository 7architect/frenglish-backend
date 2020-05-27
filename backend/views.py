from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
