from django.core.management.base import BaseCommand, CommandError
from civ.models import Users, Building, City

class Command(BaseCommand):
    args = ''
    help = 'Updates all users in the database'
    def handle(self, *args, **options):
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
            character = user.character
            profit = 0
            fcontrib = 0
            acontrib = 0
            lcontrib = 0
            bcontrib = 0
            profit = profit + city.farms*farmProfit
            profit = profit + city.labs*labProfit
            profit = profit + city.barracks*barrackProfit
            profit = profit + city.studios*studioProfit
            city.money = (character.money*profit)+city.money-city.totalpopulation
            self.stdout.write("Money: {0}\n".format(city.money))
            city.save()
            fcontrib = city.farms*(farmContrib[0] + labContrib[0] + barrackContrib[0] + studioContrib[0])*character.food
            acontrib = city.studios*(farmContrib[1] + labContrib[1] + barrackContrib[1] + studioContrib[1])*character.arts
            lcontrib = city.labs*(farmContrib[3] + labContrib[3] + barrackContrib[3] + studioContrib[3])*character.science
            bcontrib = city.barracks*(farmContrib[2] + labContrib[2] + barrackContrib[2] + studioContrib[2])*character.military
            self.stdout.write("Food Contribution: {0}\n".format(fcontrib))
            self.stdout.write("Art Contribution:  {0}\n".format(acontrib))
            self.stdout.write("Lab Contribution:  {0}\n".format(lcontrib))
            self.stdout.write("Army Contribution: {0}\n".format(bcontrib))
            fact.score = fact.score + fcontrib + 2*acontrib + 4*bcontrib + 8*lcontrib
            fact.food = fact.food + fcontrib
            fact.art = fact.art + acontrib
            fact.military = fact.military + bcontrib
            fact.science = fact.science + lcontrib
            fact.save()
            