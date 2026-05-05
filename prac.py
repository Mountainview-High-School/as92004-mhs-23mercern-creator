


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










guesses = 0
safe_points = 0
wrong_guesses = 0

while True:
 print("Which language is used for web development?")
 print("A) Python")
 print("B) HTML")
 print("C) C++")

 choice = input("Enter your choice (A/B/C): ").strip().upper()

 if choice == "B":
    print("✅ Correct! HTML is used for web page structure.")
    guesses =+ 1
    safe_points =+ 1
    
    break
 else:
    print("❌ Wrong! due to this miss step no points can be given) HTML.") 
    wrong_guesses =+ 1
    safe_points =+ -1

if wrong_guesses >= 1:
     guesses =+ -1
     wrong_guesses == 0
else:
    safe_points == 0
     

if guesses <= 0:
    guesses = 0

if safe_points == 1:
    guesses =+ 1
if safe_points == 2:
    guesses =+ 2
if safe_points == 3:
    guesses =+ 3


while True:
 print("Which language is used for web development?")
 print("A) Python")
 print("B) HTML")
 print("C) C++")

 choice = input("Enter your choice (A/B/C): ").strip().upper()

 if choice == "B":
    print("✅ Correct! HTML is used for web page structure.")
    guesses =+ 1
    safe_points =+ 1
    
    break
 else:
    print("❌ Wrong! due to this miss step no points can be given) HTML.") 
    wrong_guesses =+ 1
    safe_points =+ -1

if wrong_guesses >= 1:
     guesses =+ -1
     wrong_guesses == 0
else:
    safe_points == 0
     

if guesses <= 0:
    guesses = 0

if guesses >=1:
     print ("Well done you got " + str(guesses) + " points. " + name )
else:
    print ("better luck next time "  + name )
  