while True:
    try:
        age = int(input("please enter your age: "))
        break
    except ValueError:
        print ("seems like you put a letter in there, please try again")
if 8 <= age <= 13:
    print ("you are of age")
else:
    exit((print ("you should try the cybrsmart youth quiz instead due to your age")))
name = input("what is your name? ")
print("hello, " + name + " welcome to the quiz.")
guess = 0
wrong_guess = 0 
trys = 0

while True:
    print("someone sends you a text that is hurtful and makes you feel bad about yourself. what should you do?")
    print("A) Delete the message and try to forget about it")
    print("B) Keep the text and show an adult you trust")
    print("C) Text the person back saying something mean to them")

    choice = input("what one is the right response? (A/B/C): ").strip().upper()

    if choice == "B":
        print(f"correct " +name+ ". showing an adult you trust is the best way to deal with it")
        guess += 1
        break
    else: 
rong_guess += 1 
        trys += 1
    if trys >= 3:
        print ( ""+name+ " you have used all your trys for this question the correct answer was (B)")
        break         print ("incorrect,")
       w

if trys >= 3:
    trys = 0

if wrong_guess >= 1:
    guess -= 1
    wrong_guess = 0

if guess == -1:
    guess = 0


    print("you want to join an online gaming site. which if the following unfirmation is okay for you to post on the site.")
    print("A) A nickname")
    print("B) your name")
    print("C) your email address")

    choice = input("what one should you post? (A/B/C): ").strip().upper()
    if choice == "A":
        print(f"correct " +name+ ". using a nickname is the safest option when joining an online gaming site.")
        guess += 1
        break

    else:
        print ("incorrect")
        wrong_guess += 1
        trys += 1

    if trys >= 3:
        print ( ""+name+ " you have used all your trys for this question the correct answer was (A)")
        break

if trys >= 3:
    trys = 0

if wrong_guess >= 1:
    guess -= 1
    wrong_guess = 0

if guess == -1:
    guess = 0


    print("you find out that someone has posted an embarrassing picture of you online What should you do?")
    print("A) tweet that they are an idiot and a loser")
    print("B) ask your friends to give the person a hard time")
    print("C) tell and adult you trust")

    choice = input("what would you do in this situation (A/B/C):").strip().upper()
    if choice == "C":
        print(f"correct " +name+ ". telling an adult you trust is the best way to handle this situation.")
        guess += 1
        break

    else:
        print ("incorrect")
        wrong_guess += 1    
        trys += 1

    if trys >= 3:
        print ( ""+name+ " you have used all your trys for this question the correct answer was (C)")
        break

if trys >= 3:
    trys = 0

if wrong_guess >= 1:
    guess -= 1
    wrong_guess = 0

if guess == -1:
    guess = 0

print(f"you got {guess} out of 3 questions correct." +name+" good job")




admin = input("this is the end of the quiz.").strip().lower()
if admin == "1234":
    items = [name , str(age) , str(guess)]
else:
    exit()
message1 = "users name " + str(items[0]) + " "
message2 = "This is the users age was " + str(items[1]) + " "
message3 = "This is how many guesses the user got right: " + str(items[2]) + " "

messages = [message1, message2, message3]

for msg in messages:
    print(msg)