cars = ["bmw", "audi", "nissan"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# If you want to compare two strings without case being taken into account, convert both to lowercase
car = "Audi"
print(car.lower() == "audi")

