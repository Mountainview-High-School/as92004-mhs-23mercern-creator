while True:
    try:
        age = int(input("please enter your age: "))
        break
    except ValueError:
        print ("seems like you put a litter in ther please try again")

if 12 <= age <= 18:

   print ("you are of age")
else:
   exit((print ("you will be removed due to your age"))) 



name = input("what is your name? ")
print("Hello, " + name + "!" )

import random
number = random.randint(1, 100)
# you need to make a while loop here for this code
guess = 0
guesses = 0
while guess != number:
    guesses += 1
    guess = int(input("Guess the random number between 1 and 100: "))
    if guess > number:
        print("Your guess was too high")
    elif guess < number:
        print("Your guess was too low")

print ("Well done you got it right in " + str(guesses) + " goes. " + name + "!")