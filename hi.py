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


questionslist = ["you want to join an online gaming site. which if the following unfirmation is okay for you to post on the site.\nA) A nickname\nB) HTML\nC) C++", "someone sends you a text that is hurtful and makes you feel bad about yourself. what should you do?\nA) Delete the message and try to forget about it\nB) Keep the text and show an adult you trust\nC) Text the person back saying something mean to them","you find out that someone has posted an embarrassing picture of you online What should you do?\nA) tweet that they are an idiot and a loser\nB)ask your friends to give the person a hard time\nC)tell and adult you trust"]

answerlist = ["b", "a","c"]


wrong_guess = 0
trys = 0
guess = 0

for i in range(len(questionslist)):
  print(questionslist[i])
 
  for trys in range (3):
     choice = input("Enter your choice (A/B/C): ").strip().upper()
     if choice == answerlist[i].upper():
      print (f"✅ Correct! {answerlist[i].upper()} is the right answer.")
      guess +=1
      break
   
     else:
      print("❌ Wrong! due to this miss step no points can be given)")
      wrong_guess +=1
  if wrong_guess >= 1:
      guess -= 1
      wrong_guess = 0
  if guess <=0:
    guess == 0
 

print(f"you got {guess} out of 3 questions correct. " +name+  " good job")

