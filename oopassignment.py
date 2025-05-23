class Smartphone:
    color = "red"
    model = "Nokia"

    # Method/behaviour to display smartphone details
    def rings(self):
        print("Your phone is ringing")
    def stop(self):
        print("Your phone has stopped ringing")
 

my_smartphone = Smartphone() # Create an instance of the smartphone class
my_smartphone.rings() # Call the ring method
my_smartphone.stop() # Call the stop method
print(my_smartphone.model)  # Access the color attribute

# Self is just like a pointer to the current instance of the class










class Smartphone:
    # constructor method to initialize the object
    def __init__(self, name, releaseyear, battery):
        self.name = name  # Instance variable for name
        self.releaseyear = releaseyear    # Instance variable for releaseyear
        self.battery = battery  # Instance variable for battery

SmartphoneDetails = Smartphone("Magic Max", 2025, "17700mAh") # Create an instance of the Smartphone class

print(SmartphoneDetails.name) # Access the name attribute





# Encapsulation method 
class SecretStash:
    def __init__(self):
        self.__smartphones = 20  # Private attribute

    def sell_smartphone(self):
        if self.__smartphones > 0:
            self.__smartphones -= 2
            print("Two smartphones sold!")
        else:
            print("No smartphones left 😢")

stash = SecretStash()
stash.sell_smartphone()









# Polymorphism in action
class Car:
    def move(self):  # 
        return "Driving!"

class Aeroplane:
    def move(self):
        return "Flying!"

# Polymorphism in action
for vehicle in [Car(), Aeroplane()]:
    print(vehicle.move())