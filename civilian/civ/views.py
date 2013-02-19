from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from civ.models import Users, UserForm, Faction, City

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

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        uform = UserForm(data = request.POST)
        
        if uform.is_valid():
            user = uform.save(commit = False)
            user.set_password(user.password)
            user.name = user.username
            user.faction = Faction.objects.get(name="A")
            user.money = 2000
            user.city = City(name=user.username)
            user.save()
            registered = True
        else:
            print uform.errors
    else:
        uform = UserForm()
    
    return render_to_response('civ/register.html',{'uform':uform,'registered':registered}, context)


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect('/civ')
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print  "invalid login details " + username + " " + password
              return render_to_response('civ/login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render_to_response('civ/login.html', {}, context)

@login_required
def restricted(request):
    return HttpResponse('YOU CAN SEE THIS BIT')

@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/civ/')
