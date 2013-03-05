from civ.models import Users, Building, City

farm = Building.objects.get(buildtype="Farm")
farmProfit = farm.profit
farmContrib = [farm.pfood,farm.part,farm.pmilitary,farm.pscience]
lab = Building.objects.get(buildtype="Farm")
labProfit = lab.profit
labContrib = [lab.pfood,lab.part,lab.pmilitary,lab.pscience]
barrack = Building.objects.get(buildtype="Farm")
barrackProfit = barrack.profit
barrackContrib = [barrack.pfood,barrack.part,barrack.pmilitary,barrack.pscience]
studio = Building.objects.get(buildtype="Farm")
studioProfit = studio.profit
studioContrib = [studio.pfood,studio.part,studio.pmilitary,studio.pscience]
for user in Users.objects.all():
    city = user.city
    fact = user.fact
    profit = 0
    factcontrib = 0
    profit = city.farms*farmProfit
    profit = city.labs*labProfit
    profit = city.barracks*barrackProfit
    profit = city.studios*studioProfit
    city.money = city.money+profit-city.totalpopulation
    print city.money
    city.save()
    factcontrib = c
