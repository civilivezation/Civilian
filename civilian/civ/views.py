from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from civ.models import Users, UserForm,CityForm,UsersForm, Faction, City
from django.db.models import Min


def index(request):
    template = loader.get_template('civ/index.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

@login_required
def home(request):
    template = loader.get_template('civ/home.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

@login_required
def game(request):
    template = loader.get_template('civ/game.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        uform = UserForm(data = request.POST)
        cform = CityForm(data = request.POST)
        usersf = UsersForm(data = request.POST)
        if uform.is_valid():
            user = uform.save(commit=False)
            user.set_password(user.password)
            user.save()
            ouruser = usersf.save(commit=False)
            ouruser.user = user
            # Inserts you into a fixed faction currently
            # test = Faction.objects.all().aggregate(Min('members'))
            #fname = Faction.objects.raw('SELECT F1.name FROM Faction WHERE (Select Min(members) FROM Faction)')
            temp = -1;
            for f in Faction.objects.all():
            	if (f.members<=temp or temp<0):
            		temp=f.members
            		thename = f.name
	
            faction = Faction.objects.get(name=thename)
            faction.members = faction.members +1
            faction.save()
            ouruser.fact = Faction.objects.get(name=thename)
            ouruser.money = 2000
            city = cform.save(commit=False)
            city.name = user.username
            city.save()
            ouruser.city = city
            ouruser.save()
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
                  return HttpResponse("Your account is disabled.")
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

def live(request):
    template = loader.get_template('civ/live.html')
    fact_list = Faction.objects.all()
    context = RequestContext(request, {'fact_list': fact_list})
    return HttpResponse(template.render(context))
