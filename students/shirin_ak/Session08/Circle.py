
#-------------------
#!/usr/bin/env python3
#Session 08 Exercise:Circle class
#Shirin Akther
#-------------------------
import math

class Circle():
    def __init__(self, radius):
        # STEP 1 The radius is a required parameter
        self.radius = radius

        
    # STEP 2 Add a 'diameter' property
    @property
    def diameter(self):        
        return self.radius*2

    
    #STEP 3 set up the diameter property
    @diameter.setter
    def diameter(self, value):
        self.radius = value/2

        
    #STEP 4 Add an area property
    @property    
    def area(self):
        return math.pi * (self.radius ** 2)

    
    # STEP 5 Add an “alternate constructor” that
    #lets the user create a Circle directly with the diameter:
    @classmethod
    def from_diameter(cls, diameter):       
        return cls(diameter/2)

        
    #STEP 6 Add __str__ and __repr__ methods to your Circle class.
    
    def __str__(self): 
        return "Circle with radius: {:.4f}".format(self.radius) 

    def __repr__(self): 
        return "Circle({})".format(self.radius)

    
   #STEP 7 Add two circles and multiply one by a number
    def __add__(self, other):
      
        return self.radius + other.radius
    
    def __mul__(self, other):
        return self.radius * other

    def __rmul__(self, other):
        return self.radius * other

       
    #STEP 8 Add the ability to compare two circles
    #Once the comparing is done, you should be able to sort a list of circles
    def __greater__(self, other):
        return self.radius > other.radius
            
    def __less__(self, other):
        return self.radius < other.radius
        
    def __equal__(self, other):
       return self.radius == other.radius

    def sort_val(self):
       return self.radius

    
#STEP 9 Add a Sphere class as a subclass of Circle class
#and add and change a couple things
class Sphere(Circle): 

    """ Sphere class, inherits from Circle class """ 
    def __str__(self): 
        return "Sphere with radius: {:.2f}".format(self.radius) 


    def __repr__(self): 

         return "Sphere({})".format(self.radius)
        

    @property
    def area(self): 

        """ Returns the area of the sphere """ 
        return 4 * math.pi * (self.radius ** 2)
    
    @property
    def volume(self): 

        """ Returns the Volume of the sphere """ 
        return (4/3) * math.pi * (self.radius ** 3)





