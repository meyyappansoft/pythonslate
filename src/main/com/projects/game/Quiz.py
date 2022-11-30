print("Welcome to quiz!")
playerName = input("Enter your name : ")
if playerName == "":
    print("You have not entered your name!")
    quit()
print(playerName +  ", Lets start.")

score=0

q1 = input("What does CPU stand for? ").lower()
if q1 == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect! better luck next time..")
