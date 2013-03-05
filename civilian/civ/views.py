from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.http import *
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from civ.models import *
from django.db.models import Min
from django.utils import simplejson
from django.utils import *


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
            ouruser.character = Character.objects.get(name="Civilian")
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
            city = cform.save(commit=False)
            city.name = user.username
            city.money = 2000
            city.totalpopulation = 0
            city.workingpopulation = 0
            city.nonworkingpopulation = 0
            city.farms = 0
            city.labs = 0
            city.barracks = 0
            city.studios = 0
            city.save()
            ouruser.city = city
            ouruser.save()
            registered = True
            return user_login(request)
            
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

@login_required
def user_info(request):
    context = RequestContext(request)
    user = Users.objects.get(user = request.user)
    city = user.city
    #if (request.method == 'POST'):
    	#if request.method.value == u'Buy a residence':
    	#print request.methodvalue
        #city.money = city.money - 600
        #city.population = city.population + 1
        #city.save()
    population = city.totalpopulation
    character = user.character
    if request.method == u'GET':
        if request.is_ajax():
            GET = request.GET
            if GET.items():
                btype = GET['build']
                build = Building.objects.get(buildtype=btype)
                print build
                city.totalpopulation = city.population+build.residents
                city.money = city.money-build.money
                city.food = city.food+build.pfood
                city.art = city.part+build.part
                city.military = city.military+build.pmilitary
                city.science = city.science+build.pscience
                city.save()
                print "I'm here"
                json = simplejson.dumps({'user':user,'city':city,
                                         'character':character,
                                         'population':population})
                return HttpResponse(json,mimetype='application/json')
    context = RequestContext(request, {'user':user,'city':city,
                                       'character':character,'population':population})
    return render_to_response('civ/user_info.html',{},context)

def	suggest(request):
	context = RequestContext(request)
	user = Users.objects.get(user = request.user)
	city = user.city
        print city
	population = city.totalpopulation
	character = user.character
	btype = request.GET['build']
	if btype == '1':
		build = Building.objects.get(buildtype="House")
		if city.money < build.cost or city.nonworkingpopulation < build.workers:
			return HttpResponse(simplejson.dumps({"results":{'success':0}}))
		city.totalpopulation = city.totalpopulation+build.residents
	if btype == '2':
		build = Building.objects.get(buildtype="Farm")
		if city.money < build.cost or city.nonworkingpopulation < build.workers:
			return HttpResponse(simplejson.dumps({"results":{'success':0}}))
		city.farms = city.farms + 1
	if btype == '3':
		build = Building.objects.get(buildtype="Lab")
		if city.money < build.cost or city.nonworkingpopulation < build.workers:
			return HttpResponse(simplejson.dumps({"results":{'success':0}}))
		city.labs = city.labs + 1
	if btype == '4':
		build = Building.objects.get(buildtype="Studio")
		if city.money < build.cost or city.nonworkingpopulation < build.workers:
			return HttpResponse(simplejson.dumps({"results":{'success':0}}))
		city.studios = city.studios + 1
	if btype == '5':
		build = Building.objects.get(buildtype="Barracks")
		if city.money < build.cost or city.nonworkingpopulation < build.workers:
                    return HttpResponse(simplejson.dumps({"results":{'success':0}}))
		city.barracks = city.barracks + 1
        if build == None:
            return HttpResponse(simplejson.dumps({"results":{'success':0}}))
        print "Got to here!"
	city.money = city.money-build.cost
        print "1"
	city.workingpopulation = city.workingpopulation+build.workers
        print "2"
	city.nonworkingpopulation = city.totalpopulation-city.workingpopulation
        print "3"
	city.save()
        print "4"
        result = {'results':[1,character.title,city.money,city.totalpopulation,city.workingpopulation,city.nonworkingpopulation,city.farms,city.labs,city.barracks,city.studios]}
	return HttpResponse(simplejson.dumps(result))
