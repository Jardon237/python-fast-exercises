#using input when recieving data
from timeit import repeat

car =input("what type of car do u want ")
print(f"let me see if i can find you a {car}")

people =int(input("how many poeple are in their dinner room? "))
if people > 8:
    print("wait for a free table")
else:
    print("your table is ready")
number= int(input("enter a number "))
if number % 10 == 0:
    print("number is a multiple of 10")
else:
    print("number is not a multiple of 10")


#while loops
promt ="Tell me something and i'll repeat it to you "
same = True
while same:
    message =input(promt)

    if message =="quit":
        same = False
    else:
        print(message)
    
promt ="Enter a pizza "
message =""
while message !="quit":
    message=input(promt)
    print(message)

age=int(input("what is your age? "))
while age <=12:
    if age < 3:
        print("ticket is free")
    elif age >3 and age <12:
        print("your ticket cost $10")
    elif age > 12:
        print("your ticket cost $15")