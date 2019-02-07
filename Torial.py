

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
class Character(): #can have () and becomes more important later ##Class Name
    name = "Tin"
    sex = "Male"
    max_hit_points = 5
    current_hit_points = 5
    max_speed = 10
    armor_amount = 12
#all parts under class Character is the field/attributes

def display_character(my_character): # a field that represents the individual character
#def display_character(name, sex, max_hit_points, current_hit_points, max_soeed):
    print(my_character.name,
          my_character.sex,
          my_character.max_hit_points,
          my_character.current_hit_points)

my_dude = Character()  #() necessary ##Creates an instance of the class (Object)
###my_dude is a variable

my_dude.name = "Hina"  #Object 1 is created
# Dot operator "." Pulls out individual fields out of the object when referred to or set to something new
my_dude.sex = "Female"
my_dude.max_hit_points =25

his_dude = Character()  #Object 2
his_dude.name = "Roy"

display_character(my_dude)
display_character(his_dude)

class Address():
    """ Hold all the fields for a mailing address. """
    def __init__(self):
        """ Set up the address fields. """
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""


# Create an address
home_address = Address()

# Set the fields in the address
home_address.name = "John Smith"
home_address.line1 = "701 N. C Street"
home_address.line2 = "Carver Science Building"
home_address.city = "Indianola"
home_address.state = "IA"
home_address.zip = "50125"

# Create an address
my_address = Address()

# Alert! This does not set the address's name!  ##Variable
name = "Dr. Craven"

# This doesn't set the name for the address either
Address.name = "Dr. Craven"    #Sets the address' name

# This does work:
my_address.name = "Dr. Craven"

# Create another address
vacation_home_address = Address()

# Set the fields in the address
vacation_home_address.name = "John Smith"
vacation_home_address.line1 = "1122 Main Street"
vacation_home_address.line2 = ""
vacation_home_address.city = "Panama City Beach"
vacation_home_address.state = "FL"
vacation_home_address.zip = "32407"

print("The client's main home is in " + home_address.city)
print("His vacation home is in " + vacation_home_address.city)
print("His name is " + my_dude.name)

#####Methods of Classes
class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):  ##Method, addition of self
        print("Woof")
        #Note:
        # Attributes should be listed first, methods after.
        # The first parameter of any method must be self.
        # Method definitions are indented exactly one tab stop.

my_dog = Dog()  #Creates the dog

my_dog.name = "Toad"
my_dog.weight = 20
my_dog.age = 3
#^^^Sets the object attributes

my_dog.bark()

def bark(self):
    print("Woof says", self.name)
