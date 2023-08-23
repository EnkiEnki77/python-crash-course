# In OOP you create classes that represent real world things, and situations.
# And you create objects based on these classes. When you write a class you define the general behaviour a whole 
# category of objects can have.

# When you create individual objects from the class they automatically have that general beheaviour, and you can then 
# give each object whatever unique traits you want.

# Making an object with a class is called instantiation, and you work with instances of a class. 

# classes can also extend other classes, and be imported from a module.

# When creating a class for something, lets say a dog. Think about the info and behaviours all dogs would have. Such as
# name and age for info, and bark and roll over for behaviour. info will be data initialized in the constructor. Behaviours
# will be the classes methods. You should give every class a docstring

# class names should be capitalized
class Dog:
    """A model for a dog"""

    # The __init__ method is a special method run whenever a new instance of a class is created.
    # And is also known as the constructor method 
    # The self param is required in the constructor, and should always be the first param. This param must be included
    # because when python calls the constructor it will automatically pass the value for self.
    # In fact every method called from the instance automatically gets self passed to it, so it must be included if 
    # if the method needs to reference some sort of data stored in the instance. self gives the instance access to 
    # the attributes and methods of the class.
    # When you instantiate a class you have the option to pass it arguments, those additional arguments are passed to 
    # __init__ when its called and populate whatever params where defined for __init__ other than self.

    def __init__(self, name, age):
        """Initial age and name attributes"""
        # Properties are defined in the __init__ method. Any properties prefixed with self are available throughout the
        # entire class. Self represents the object instance, we are creating properties for that instance.
        # Variables that are accessible through instances like below are called attributes. 
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name.title()} is now sitting.")

    def rollover(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name.title()} rolled over")

# Think of a class as a set of instructions to create an instance.
# Below we make a call to the Dog class, python automatically calls the __init__ method with the arguments "tank" and 5
# The __init__ method creates an instance of the class with the attributes name and age, assigned the values of the methods
# params. The instance is returned and stored in the variable my_dog
my_dog = Dog("tank", 5)
# To access an instances attributes and methods you utilze dot notation. 
# Remember self is passed to every method called from a class or instance, and it represents the instance.
print(f"{my_dog.name.title()} is my dogs name, he is {my_dog.age} years old")

# Descriptive names allow us to infer what something is doing
my_dog.sit()

# You can create as many instances from a class as youd like
your_dog = Dog("lillie", 3)
print(f"{your_dog.name.title()} is my dogs name, he is {your_dog.age} years old")
your_dog.sit()


