 
class Dog:

    def __init__(self, name, age):
          self.name = name
          self.age = age #attribute

    def sit(self):
        print(f"{self.name} is now sitting.") #methods

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog=Dog("will", 6)
your_dog=Dog("jake", 3) #instance
print(f"my dog is called {my_dog.name}")
print(f"it is {my_dog.age}")
my_dog.sit() #calliung back the method

print(f"your dog is called{your_dog.name}")
print(f"it is {your_dog.age}")
your_dog.roll_over() #calling abck the method