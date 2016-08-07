import random
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name=name
        self.location=tuple(map(float,location))
        self.species_types=species_types
         
    def get_number_of_species(self, animal):
        if animal in self.species_types:
            return self.species_types[animal]
        else :
            return 0
    
    def get_location(self):
        return self.location
    
    def get_species_count(self):
        newcopy=self.species_types.copy()
        return newcopy
    
    def get_name(self):
        return self.name
        
    def adopt_pet(self, species):
        if species in self.species_types:
            if self.species_types[species]>0:
                self.species_types[species]-=1
            if self.species_types[species]==0:
                del self.species_types[species]
        else :
             return 0

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name=name
        self.desired_species=desired_species
        
    def get_name(self):
        return self.name
        
    def get_desired_species(self):
        return self.desired_species
        
    def get_score(self, adoption_center):
            num_desired=adoption_center.get_number_of_species(self.desired_species)
            return float(num_desired)
            
class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self,name,desired_species)
        self.considered_species=considered_species
    def get_score(self,adoption_center):
        num_other=0
        for i in self.considered_species:
            num_other+=adoption_center.get_number_of_species(i)
        adopter_score=adoption_center.get_number_of_species(self.desired_species)
        score=adopter_score+0.3*num_other
        return score
class FearfulAdopter(Adopter):
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self,name,desired_species)
        self.feared_species=feared_species
    def get_score(self,adoption_center):
        num_feared=adoption_center.get_number_of_species(self.feared_species)
        adopter_score=adoption_center.get_number_of_species(self.desired_species)
        score=adopter_score-0.3*num_feared
        if score<0:
            score=float(0)
        return score
class AllergicAdopter(Adopter):
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self,name,desired_species)
        self.allergic_species=allergic_species
    def get_score(self,adoption_center):
        some_value=adoption_center.get_species_count()
        for i in self.allergic_species:
            if i in some_value:
                score=0.0
                return score
        adopter_score=adoption_center.get_number_of_species(self.desired_species)
        return float(adopter_score)
class MedicatedAllergicAdopter(AllergicAdopter):
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness=medicine_effectiveness
    def get_score(self,adoption_center):
        kidilam=adoption_center.get_species_count()
        machan=self.medicine_effectiveness.copy()
        adopter_score=adoption_center.get_number_of_species(self.desired_species)
        while machan!={}:
            adipoli_small=min(machan, key=machan.get)
            if adipoli_small in kidilam.keys():
                score=adopter_score*machan[adipoli_small]
                del machan[adipoli_small]
                return score
            else:
                del machan[adipoli_small]
        return float(adopter_score)
class SluggishAdopter(Adopter):
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self,name,desired_species)
        self.location=tuple(map(float,location))
    def get_linear_distance(self,to_location):
        there=to_location.get_location()
        here=self.location
        distance=((there[0]-here[0])**2+(there[1]-here[1])**2)**.5
        return distance
    def get_score(self,adoption_center):
        distance=self.get_linear_distance(adoption_center)
        adopter_score=adoption_center.get_number_of_species(self.desired_species)
        if distance<1:
            return adopter_score
        elif distance<3 and distance>=1:
            some=random.uniform(.7, .9)
            return some*adopter_score
        elif distance<5 and distance>=3:
            some=random.uniform(.5, .7)
            return some*adopter_score
        elif distance>5:
            some=random.uniform(.1, .5)
            print some
            return some*adopter_score
from operator import itemgetter, attrgetter

def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    new_list=[]
    mini_list=[]
    ordered_list=[]
    for i in list_of_adoption_centers:
        score=adopter.get_score(i)
        mini_list=[i,score]
        new_list.append(mini_list)
    newList=sorted(new_list, key=itemgetter(0))
    newList=sorted(new_list, key=itemgetter(1),reverse=True)
    for i in newList:
        ordered_list.append(i[0])
    return ordered_list
        
def get_adopters_for_advertisement(adoption_center, list_of_adopters,n):
    new_list=[]
    mini_list=[]
    ordered_list=[]
    list_of_adopters=sorted(list_of_adopters, key=attrgetter('name'))
    for i in list_of_adopters:
        score=i.get_score(adoption_center)
        mini_list=[i,score]
        new_list.append(mini_list)
    newList=sorted(new_list, key=itemgetter(1),reverse=True)
    for i in newList:
        ordered_list.append(i[0])
    return ordered_list[:n]


           
sleeba=AdoptionCenter('sleeba',{"Dog": 10, "Cat": 5, "Lizard": 3},(-5,-1))
nimmy=AdoptionCenter('nimmy',{"Dog": 18, "Hen": 2, "Squirrel": 8},(-.2,-1))
aleyamma=AdoptionCenter('aleyamma',{"Dove": 50, "Mouse": 5, "Lizard": 3},(-1,-1))
alist=[sleeba,nimmy,aleyamma]
mypet=Adopter('Nimmy','Dog')
foo=MedicatedAllergicAdopter('Nimmy','Dog',['Lizard','Cater'],{"Cater": 0.5, "Lizard": .75})
newpet=SluggishAdopter('Nimmy','Dog',(.3,1))


adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))
#print get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])
 
adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

print get_adopters_for_advertisement(ac2, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6],6)