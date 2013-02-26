from django_cron import cronScheduler as cron, Job

from civ.models import Character, Building, Users, Faction


class UpdateAll(Job):
    run_every = 15
    
    def job(self):
        print "I'm here!"
        for fact in Faction:
            fact.members = fact.members +1
            fact.save()
        for user in Users:
            char = user.character
            city = user.city
            city.money = (city.food*Building.objects.get(buildtype="Farm").profit*char.food)
            

cron.register(UpdateAll)
