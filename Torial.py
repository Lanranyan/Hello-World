
""" CLASSES """
### Help reuse code, convenient to change code, allow for more flexible functions
# Classes make objects and the functions in a class become the object’s methods
# A class is a “classification” of an object. Like “person” or “image.”
# An object is a particular instance of a class. Like “Mary” is an instance of “Person.”
#Objects have attributes, such as a person's name, height, and age. Objects also have methods. Methods define what an
# object can do, like run, jump, or sit.
# Each character in an adventure game needs data: a name, location, strength, are they raising their arm,
# what direction they are headed, etc. Plus those characters do things. They run, jump, hit, and talk.

#ClassOne.py
#### Part 1 from https://www.afterhoursprogramming.com/tutorial/python/classes/
class Calculator(object):
    #defines class to simulate a simple calculator
    def __init__(self):
        #starts with 0 and creates an instance of the class to differentiate
        self.current = 0
            #Creates a variable instance equal to 0
    def add(self, amount):
        # add number to current
        self.current += amount
    def getcurrent(self):
        return self.current

mybuddy = Calculator()  #make myBuddy into a Calculator object
mybuddy.add(2)  ##use myBuddy's new add method derived from the Calculator class
print(mybuddy.getcurrent()) #print myBuddy's current instance variable


##### Part 2 of Classes from http://programarcadegames.com/index.php?chapter=introduction_to_classes&lang=en#section_12
class Character(): #can have () and becomes more important later
name = "Tin"
    sex = "Male"
    max_hit_points = 5
    current_hit_points = 5
    max_speed = 10
#all parts under class Character is the field

my_dude = Character()  #() necessary

my_dude.name = "Hina"
my_dude.sex = "Female"
my_dude.max_hit_points =25

def display_character(my_character): # a field that represents the individual character
#def display_character(name, sex, max_hit_points, current_hit_points, max_soeed):
    print(name, sex, max_hit_points, current_hit_points)


