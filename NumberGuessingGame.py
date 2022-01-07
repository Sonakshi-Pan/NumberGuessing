import random
print("Number Guessing game")

number = random.radint(1,9)
chances=0
print("guess a number (between 1 and 9) :")

while chances < 5 :
    guess=int(input("enter your guess:-"))

    if guess == number:
        print("congratulation you won !!")
        break

    elif guess < number:
        print("Your Guess is too low .Try some higher value",guess)
      
    else:
        print("Your guess is too high. Try some lower value",guess)
        
    chances +=1  

if not chances <5:
    print("You Lose!! the number is :",number)


