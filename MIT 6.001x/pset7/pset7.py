import random as rand
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
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
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
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
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
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
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
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
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
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
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
            some=rand.uniform(.7, .9)
            return some*adopter_score
        elif distance<5 and distance>=3:
            some=rand.uniform(.5, .7)
            return some*adopter_score
        elif distance>5:
            some=rand.uniform(.1, .5)
            print some
            return some*adopter_score

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
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

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
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

