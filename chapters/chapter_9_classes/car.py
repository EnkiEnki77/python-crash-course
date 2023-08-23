class Car:
    """A class that represents a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # You can define default attributes that dont get their value from a param
        self.odometer_reading = 0
        

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print statement showing the cars mileage"""
        print(f"The mileage is {self.odometer_reading}")

    def update_odometer(self, mileage):
        """Updates mileage on odometer. Reject the change if the odometer is attempted to be rolled back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You cant roll back the odometer.")

    def increment_odometer(self):
        """Increment the odometer by 100 miles"""
        self.odometer_reading += 100

    def fill_gas_tank(self):
        """Fill up gas tank of car."""
        print("Gas tank filled.")
    

my_car = Car("Nissan", "370Z", 2012)

print(my_car.get_descriptive_name())
my_car.read_odometer()

# There are three ways to modify an instances attributes
# 1. modify it directly
my_car.odometer_reading = 23
my_car.read_odometer()

# 2. Updating the attribute through a method
my_car.update_odometer(37)
my_car.read_odometer()

# 3. incrementing an attribute through a method. Use methods like this to control how a user updates an attribute.
my_car.increment_odometer()
my_car.read_odometer()
