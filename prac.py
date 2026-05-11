


from typing import Self


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
print("Hello, " + name + "! Welcome to the quiz.")

while True:
 print("Which language is used for web development?")
 print("A) Python")
 print("B) HTML")
 print("C) C++")

 choice = input("Enter your choice (A/B/C): ").strip().upper()

 if choice == "B":
    print(f"✅ Correct! HTML is used for web page structure.")
    break
 
 else:
    print("❌ Wrong! due to this miss step no points can be given) HTML.") 
