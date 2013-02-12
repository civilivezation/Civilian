from django.http import HttpResponse

def index(request):
    return HttpResponse("CIVILIAN")

def home(request):
    return HttpResponse("HOME")
