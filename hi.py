



items = [name , str(age) , str(guess)]

message1 = "users name " + str(items[0]) + " "
message2 = "This is the users age was " + str(items[1]) + " "
message3 = "This is how many guesses the user got right: " + str(items[2]) + " "

# Store the variables directly, without quotes
messages = [message1, message2, message3]

for msg in messages:
    print(msg)