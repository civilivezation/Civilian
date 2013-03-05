from civ.models import Building, City

farmProfit = Building.objects.get(buildtype="Farm").profit
labProfit = Building.objects.get(buildtype="Farm").profit
barrackProfit = Building.objects.get(buildtype="Farm").profit
studioProfit = Building.objects.get(buildtype="Farm").profit


for city in City.objects.all():
    city.money = city.money + city.farms*farmProfit
    city.money = city.money + city.labs*labProfit
    city.money = city.money + city.barracks*barrackProfit
    city.money = city.money + city.studios*studioProfit
    print city.money
