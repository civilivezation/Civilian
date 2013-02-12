from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    return HttpResponse("CIVILIAN")

def home(request):
    template = loader.get_template('civ/home.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def game(request):
    template = loader.get_template('civ/game.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))
