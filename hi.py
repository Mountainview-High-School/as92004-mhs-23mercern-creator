thislist = ["you want to join an online gaming site. which if the following unfirmation is okay for you to post on the site.\nA) A nickname\nB) HTML\nC) C++", "someone sends you a text that is hurtful and makes you feel bad about yourself. what should you do?\nA) Delete the message and try to forget about it\nB) Keep the text and show an adult you trust\nC) Text the person back saying something mean to them"]

answerlist = ["b", "a"]


for i in range(len(thislist)):
  print(thislist[i])
  choice = input("Enter your choice (A/B/C): ").strip().upper()
  if choice == answerlist[i].upper():
        print(f"✅ Correct! {answerlist[i].upper()} is the right answer.")
        continue
  else:
        print("❌ Wrong! due to this miss step no points can be given)")