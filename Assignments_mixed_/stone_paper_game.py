"""" Stone paper game"""

import random
user_action = input("Enter a choice(rock,paper,scissors):")
posi_actions = ["rock", "paper", "scissors"]
bot_actions = random.choice(posi_actions)
print(f"your choice {user_action}, bot choice {bot_actions}")
def game(user_action):
    if user_action==bot_actions:
        print(f"both are {user_action}. it's a tie!")
    elif user_action=="rock":
        if bot_actions=="scissors":
            print(f"rock smashes scissors! you win!")
        else:
            print(f"paper covers rock! you lose.")
    elif user_action=="paper":
        if bot_actions=="rock":
            print(f"paper covers rock! you win!")
        else:
            print(f"scissors cut paper! you lose.")
    elif user_action=="scissors":
        if bot_actions=="paper":
            print(f"scissors cut paper! you win!")
        else:
            print(f"rock smashes scissors! you lose.")
game(user_action)