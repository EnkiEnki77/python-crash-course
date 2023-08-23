# You dont always have to write classes from scratch, if a class is a specialized version of another you can 
# use inheritance. When a class inherits from another it takes on the attributes and methods of the class its 
# inheriting from. The first class is called the parent, the one inheriting is the child. The child can inherit 
# some or all of its parents attributes/methods, but can also define its own.

# When you inherit from a class the parent must be apart of the same file and come before the child.
# The name of the parent must be included in parens of the definition of the child
# The __init__ method takes in the info re/ quired to make the parent class
from car import Car

# The subclass must take in its parent as argument
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric cars"""

    # the init method must take in all arguments required for parent
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class then initialize attributes specific to an electric car."""
        # The super method is a special method that allows you to call methods from the parent class, this allows
        # you to call the parent classes __init__, giving the subclass instance all of the parents attributes. The super
        # name comes from the convention of calling the parent class a superclass and the child a subclass
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"The battery size is {self.battery_size}-khw")

    # You can overwrite any method of a parent class that may not make sense for the child class by making a version
    # in the child class.
    # When using inheritance you can retain what you need and override anyting you dont in a child class.
    def fill_gas_tank(self):
        """Electric cars dont have gas tanks"""
        print("This car doesnt have a gas tank.")

# Sometimes you may notice your classes are getting lengthy from lots of attributes and methods, and that maybe part of
# your class could be written as a seperate class. you can then use these claasses to work together. This is called 
# composition. You can use instances of other classes as attributes in your class.
class Battery:
    """A model battery for an electric car."""
    def __init__(self, battery_size=50):
        """Initialize the batteries attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the cars battery"""
        print(f"This car has a {self.battery_size}-khw size battery.")

    def get_range(self):
        """Describe the range of the car based on its battery size"""
        if self.battery_size == 50:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car has a {range} mile range at full charge.")

my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
# When using instances as attributes you have to access the attribute to access its methods. You should name the attribute
# after the class.
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()

# Try to think about the best way to model your classes to best represent the real world object or situation. think 
# about what classes certain attributes/methods should actually belong to. 
