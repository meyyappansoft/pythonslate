import random

top_range = input("Type a Number : ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type a number")
    quit()

random_number  = random.randint(0, top_range)
number_of_guess = 0

while True:
    number_of_guess +=1
    user_guess = input("Enter your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number next time..")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("Wrong guess, you were above the number..")
        else:
            print("Wrong guess, you were below the number")

print("you got it in ", number_of_guess)
