class Parent(object): 
    def init(self, xyz):
        ''' do something '''
    def build_somthing(self, abc):
        '''
        build somthing 
        '''
        return something

    def use_build(self, abc):
        '''
        This is an example of using build_something within the same class
        '''
        myThing = self.build_something(abc)
        myToy = myThing.copy()### make myToy from myThing
        return myToy  
class Child(Parent):
    def __init__(self, xyz, abc):
        '''
        child class extended from parent
        '''
        Parent.__init__(self, xyz)
        self.abc = abc

    def get_something_from_parent(self):
        '''
        This is an example of using Parent method of build_something()
        thru inheritance
        '''
        self.newthing = self.build_something(self.abc)
        return ### proper things should be returned
