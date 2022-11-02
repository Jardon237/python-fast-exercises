from curses import beep
import random
import sys
while True:
    print("name")
    name = input()
    if name == "Jude":
        print("hello Jude enter your password")
        pass_word = input()
        if pass_word == "less":
            break
print("thank you" + name)



secret_number = random.randint(1,20)
print("I am thinking of a secrete number")

for guess in range (1, 7):
    print("take a guess")
    guess = int(input())

    if guess == secret_number:
        print("good job you guessed my number in" + str(guess) + "guesses")
    elif guess < secret_number:
        print("your guess is too small")
    elif guess > secret_number:
        print("your guess is too high")
    else:
        break
print("Nope the number i was thinking is" +str(secret_number))

        
# both programs take a special value or charactewr before the program gets to completoins