is_hot = True

if is_hot:
    print("its a hot day ")
    print("drink plenty of water")
elif is_cold:
    print("its a coldnday")
    print("wear warm clothes")
else:
    print("enjoy your day")


#some if statements
has_good_credi = True

if has_good_credit:
    down_payment = (10/100) * 1000000
    print(down_payment)
else:
    down_payment = (20/100) * 1000000
    print(down_payment )


temp = 30

if temp > 30:
    print('its a hot day')
#elif:
    temp < 10
    print("its a cold day")
else:
    print('its neither not nor cold')  



#program to check length of name
Name = 'Ngwa Jude Achangwa'

if (len(Name)< 3):
    print("name mus be atleast 3 characters")
elif(len(Name)> 50):
    print("name must be atleast 50 characters")
else:
    print("name looks good")


#weigth coventer

weight = input("enter your weight")
unit = input("(L)bs or (K)g")

if unit == "K":
    new_weight = float(weight * 0.23)
    print(f"you are {new_weight} kilos")
elif unit == "L":
    new_weight = float(weight / 0.23)
    print(f"you are {new_weight} pounds")

#using loops  
 secrete= 9
 guess = 0
 guess_end = 3
 while guess < guess_end:
     guess_1 = int(input('Guess:'))
     guesss += 1
     if guess == secrete:
         print("you won")
         break


