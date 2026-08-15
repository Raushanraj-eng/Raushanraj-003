
from random import random

import random
P1_score = 0
C1_score = 0
n=int(input("Enter the number of rounds you want to play: "))
choices = ["rock", "paper", "scissors"]
for i in range(n):
 player = input("Enter your choice (rock, paper, scissors): ").lower() 

   
 computer = random.choice(choices)

 print(f"Computer chose: {computer}")
 print(f"Your choice: {player}")
 print("______________________________________________________________________")
 print(f"Round {i+1}:")

 if player == computer:
    print("It's a tie!")
 elif(player,computer)in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
    print("You win this round!  (^_^) ") 
    P1_score += 1
 else:
    print("Computer wins this round! |-_-|")
   
    C1_score+=1
print("______________________________________________________________________")  

print(f"Your score: {P1_score}/{n}")
print("______________________________________________________________________")
print(f"Computer's score: {C1_score}/{n}")

if P1_score > C1_score:
    print("Congratulations! You won the game!")
elif P1_score < C1_score:
    print("Your luck not with you this time .")
elif P1_score == C1_score:
    print("It's a tie!  so close to win.")