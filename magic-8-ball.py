import random

name = input("Tell me your name: ")

if name == "":
    name = "Mysterious Stranger"
print("Welcome " + name)

print("The Magic 8 Ball will answer any question you have about the future")

question = input("Ask the 8 ball a question about the future: ")
if question == "":
    print("The Magic 8 Ball respects your decision to not pry into the workings of fate")
else: print(name + " asks the magic 8 Ball: " + question)

answer = ""

random_number = random.randint(1,9)
# print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else: answer = "Error"


if question != "":
    print("Magic 8-Ball's answer: " + answer)