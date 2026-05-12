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
    print("hello, " + name + "! welcome to the quiz.")




while true:
    print("someone sends you a text that is hurtful and makes you feel bad about yourself. what should you do?")
    print("A) Delete the message and try to forget about it")
    print("B) Keep the text and show an adult you trust")
    print("C) Text the person back saying something mean to them")

    choice = input("what on is the right response? (A/B/C): ").strip().upper()

    if choice == "B":
        print(f:"correct showing an adult you trust is the best way to deal with it")
        break
    else: 
        print ("incorrect,")