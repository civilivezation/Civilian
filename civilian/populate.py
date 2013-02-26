from civ.models import Faction, Building, Character

F = Faction(name="A",members=0,score=0)
F.save()
F = Faction(name="B",members=0,score=0)
F.save()
F = Faction(name="C",members=0,score=0)
F.save()
B = Building(buildtype="House",cost=600,profit=-50,residents=50,
             workers=0,pfood=0,part=0,pmilitary=0,pscience=0)
B.save()
B = Building(buildtype="Farm",cost=1000,profit=200,residents=0,
             workers=30,pfood=20,part=0,pmilitary=0,pscience=0)
B.save()
B = Building(buildtype="Lab",cost=4000,profit=400,residents=0,
             workers=40,pfood=0,part=0,pmilitary=0,pscience=20)
B.save()
B = Building(buildtype="Barracks",cost=2500,profit=300,residents=0,
             workers=70,pfood=0,part=0,pmilitary=25,pscience=0)
B.save()
B = Building(buildtype="Studio",cost=3200,profit=200,residents=0,
             workers=10,pfood=0,part=30,pmilitary=0,pscience=0)
B.save()
C = Character(name="Scientist",title="Dr.",cost=6000,money=1.1,
              food=1,science=1.2,military=1.1,arts=0.9)
C.save()
C = Character(name="Warrior",title="The Conquering",cost=3500,money=1.15,
              food=0.9,science=0.9,military=1.3,arts=0.8)
C.save()
C = Character(name="Gentleman",title="Sir",cost=7000,money=1.3,
              food=0.85,science=0.9,military=1.05,arts=1.15)
C.save()
C = Character(name="Pirate",title="Long-John",cost=1000,money=1.2,
              food=0.9,science=0.7,military=1.15,arts=0.8)
C.save()
C = Character(name="Evil-doer",title="Count von",cost=20000,money=1.5,
              food=0.3,science=1.5,military=1.5,arts=0.3)
C.save()
C = Character(name="Politician",title="President",cost=4000,money=0.8,
              food=0.9,science=1.1,military=1.1,arts=1.2)
C.save()
C = Character(name="Emporer",title="Emporer",cost=10000,money=1.1,
              food=1.25,science=0.8,military=1.1,arts=1.1)
C.save()
C = Character(name="Civilian",title="Citizen",cost=0,money=1,
              food=1,science=1,military=1,arts=1)
C.save()
