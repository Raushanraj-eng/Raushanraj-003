import random
number = random.randint(1, 10)
print("_________________________________________Welcome to the Guessing Game!_________________________________")
print("you have only 3 chances ")

for i in range(3):
    guess=int(input("Enter your guess: "))
    if guess==number:
        print("you win! ")
        break
    elif guess>number:
        print("Too high")  

    elif guess<number:
        print("Too low")
else :
    print("you lost")
    print(f"number was {number}:")