# You should place each class into its own module and import them in as needed to keep things  as organized and 
# uncluttered as possible.
# Just as every function should have its own docstring, so should each module, to describe what the module is for.
"""A class used to represent a car"""

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