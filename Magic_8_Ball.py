import random
random_number = random.randint(1,10)


name= "Ludo"
question= "5 is more than 10?"
answer=""


if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9 :
  answer = "Very doubtful"
elif random_number == 10:
  answer = "bellaaa"
else:
  answer = "Error"


if name == "":
  print("Question:",question)
elif question == "" or len(question) == 0:
  print("You didn't ask any question now!")
else:
   print(name + " asks: " + question)

if name != "" and question != "":
  print("Magic 8-Ball's answer:", answer)
else:
 print("I can't give you an answer")
