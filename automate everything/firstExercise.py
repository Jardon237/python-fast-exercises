import numbers


spam=0
print("input spam")
spam = int(input()) 
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings")

for numbers in range(1,11):
    print(numbers, end="")

number = 0
while number < 11:
    print(number)
    number = number+1