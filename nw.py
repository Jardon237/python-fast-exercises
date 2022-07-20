from ast import And, FloorDiv
from optparse import Values
import this

#working with varaibles
message="you are useless"

message="reall use less"
print(message)

#working with strings
first_name="ada lovelace"
last_name ="Jude"
print(first_name.title()) #using the .title methiod to change the case of the case
print(first_name.upper()) #changinr the entire first_name to upper case
print(first_name.lower()) #Changing all to lowe case

print(f"{first_name} {last_name.title()}") #using formated string 

print("languages: Python \n java \n c\n R") #Using the escape character \n to move to a new line

from email.policy import strict


name ="Eric"
print(f"Hello {name} would you like to learn some python today?")
print(name.title())
print(name.upper())
print(name.lower()) 

famous_person = "Albert Einstein"
print(f"{famous_person} once said, 'A person who never made a mistake never tried anything new'")
stripping =" Jude "
print(f"name:\n {stripping}")
print(stripping.rstrip())
print(stripping.strip())
print(stripping.lstrip())

#working with numbers
2 + 3 
3 - 2
3/2
10 ** 6  # intergers
10 * 6
(2+3) * 4

0.1 #floats
number=8
print(number + 7 * 4 - 5 / number)
print(f"my favorite number is {number}")

#this is a comment
'''this is a mul;tiple line comment'''


#list
Friend=["drew", "nkini", "adi", "laura","zack", "mark", "steve"]
print(Friend[0])
print(f"i would prefer {Friend[1].title()} to all")

Friend[0]="vince"
Friend.append("Ebenezar")
Friend.pop(-2)
del Friend[2]
print(Friend)

Guest_list= ["john", "peter", "james", "paul"]
print(f"{Guest_list[0].title()} you are invited for a dinner")
print(f"{Guest_list[1].title()} you are invited for a dinner")
print(f"{Guest_list[2].title()} you are invited for a dinner")
print(f"{Guest_list[3].title()} you are invited for a dinner")
Guest_list.pop(2)
Guest_list.append("bih")
Guest_list[3]="new"
Guest_list.append("trash")
print(Guest_list)

# looping through an entire list
pizzas =['pepperoni', 'jinjer', 'tomatoe', 'nular']
for pizza in pizzas:
    print(f" i like {pizza.title()} pizza \n")
print("my love for pizza is immeaqsurable to anything on earth")

animals =['dog', 'cat', 'rabbit', 'rat']
for animal in animals:
    print(f"A {animal.title()} will make a great pet \n")
print("these are the best pets i know so far")
 
 #making numerical list
for values in range(1, 21):
    print(values)
    
one_milion=[]
for values in range (1, 10000001):
    one_milion.append(values)
   # print(one_milion)
min(one_milion)
max(one_milion)

odd=[]
for values in range (1,20,2): # odd numbers from 1 to 20
    odd.append(values)
print(odd)

threes=list(range(3,30,3)) #printing multiples of 3
print(threes)

cube=[]
print (cube)

#working with part of a list
print("my firts friends are")
for Friend in Friend[:3]:
    print(Friend)

print("my middle friends are")
for Friend in Friend[1:4]:
    print(Friend)

print("my last friends are")
for Friend in Friend[2:5]:
    print(Friend)

frind_pizza =pizzas[:]
frind_pizza.append("egg")
print(frind_pizza)
print(f"my favorite pizzas are")
for pizza in pizzas:
    print(pizza)
print("my friend's favourite pizzaS are:")
for frind_pizza in frind_pizza:
    print(frind_pizza)

#tuples (fixed list)
foods=("rice", "beans", "spaghetti", "plantains", "yams")
print('\n These are the avialable foods we have today')

for food in foods:
    print(food)
#foods[0]="g.nut soup"
foods=("rice", "beans", "spaghett", "plantains", "irish")
print("this is the menu for today")
for food in foods:
    print(food)
#If statements
car ="bmw"
print("Is car =='bmw'? i predict True.")
print(car =='bmw')

print ("\n is car =='audi'? i predict false")
print(car =='audi')
   
print (3 < 2)
print (3 == 2)
print( 3 <= 3)
print
print(car.lower() =="bmw")

print("rice" in foods)
print("pork" in foods)


