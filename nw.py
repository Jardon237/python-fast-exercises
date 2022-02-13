'''
print("Ngwa jude")
print("o----")
print("|||||")
print("*" * 10)

#input
birth_year = int(input('whats your birth year? '))
print(type(birth_year))
age = 2021 - birth_year
print(type(age))
print(age)

K= float(input("what is your weght in kilos? "))
L= float(input('what is your weight in pounds? '))

if (K):
    coverted = L* 0.5
    print(f"you are {coverted} kilos")
else:
    coverted = K /0.5
    print(f"you are {coverted} pounds") 
StopAsyncIteration 

#strings
course = 'Python'
print(len(course)) #len is a method
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('P')) #returns index
print(course.replace('P', 'J')) #replace method replaces a word or letter in a string
print('Python' in course) #in operator returns a boolean value 

#math functions
import math
print(math.ceil(2.9))
print(math.flooor(2.9))
x  =2.9
print(round(x))
print(abs(-2.9)) 

#if statements
Is_hot = True
is_cold = True
if Is_hot:
    print("its a hot day")
    print('drink plenty of water')
elif is_cold:
    print('its a cold day')
    print('wear warm clothes')
else:
    print("its alovely day") 

Has_good_credit =True
price = 1000000
if Has_good_credit:
    down_payment = int(0.1 * price)
    print(f"your down payment is ${down_payment}")
else:
    down_payment = int(0.2 * price)
print(f"your down payment is ${down_payment}") 


#comparison operator
name = 'Ngwa Jude'
if len(name) < 3:
     print("name must be 3 characters")
elif len(name) > 50:
    print('name can be 50 characters max')
else:
    print('name loooks good')



old = int(input("enter old meter reading "))
new = int(input("enter new mater reading "))
vat = 600
tax = 50
unit = new - old
unit_consumption = unit * vat
if unit > 7:
    price =  unit * tax
    print(price)
   

def area_of_trapezium(a,b,h):
    area = 0.5 * (a + b) * h
    print (f"area of trapezium{area}")
def main():
    area_of_trapezium(10, 15, 20)

if __name__ == "__main__":
    main()

test_varaible = 5
def outer_function():
    test_varaible = 10
    def inner_function():
            test_varaible =100
            print(f"local variable of {test_varaible} having inner function ")  
    inner_function()
    print(f"local varaible of {test_varaible} having outer function")
outer_function()
print(f"global variable of {test_varaible}")

def combined_area(a,b):
    def area_of_cube(x):
        return 6*pow(x,2)
    return area_of_cube(a)+ area_of_cube(b)
def main():
    result=combined_area(2,3)
    print(f"{result}")

if __name__ == "__main__":
    main()

i = 0
while i<10:
    i = i+1
    print(i)
  '''

numbers = [6 ,2 ,5 ,2, 2]

for number in numbers:
    print("x"* number)