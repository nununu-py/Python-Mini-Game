import random
ROCK = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

PAPER = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

SCISSORS = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

global game_option
global user_score, computer_score

user_score = 0
computer_score = 0
game_option = [ROCK, PAPER, SCISSORS]


# computer

def computer_turn():

    choice = random.choice(game_option)

    return choice


# user

def user_turn():

    print("Please insert ONLY int 1 - 3. (1. Rock | 2. Paper | 3. Scissor )")
    valid_input = [1, 2, 3]

    choice = int(input("1. Rock 2. Paper 3.Scissors : "))

    if choice in valid_input:

        return game_option[choice - 1]

    else:

        return "Invalid User Input"


# compare user and computer choice

def result(u, c: str):

    global computer_score, user_score

    if u == c:
        return f"Tieee.. Your Score = {user_score} || Computer Score = {computer_score}"

    elif u == ROCK:

        if c == PAPER:
            computer_score += 1
            return f"Computer Win.. Your Score = {user_score} || Computer Score = {computer_score}"
        else:
            user_score += 1
            return f"You Win.. Your Score = {user_score} || Computer Score = {computer_score}"

    elif u == PAPER:

        if c == SCISSORS:
            computer_score += 1
            return f"Computer Win.. Your Score = {user_score} || Computer Score = {computer_score}"
        else:
            user_score += 1
            return f"You Win.. Your Score = {user_score} || Computer Score = {computer_score}"

    elif u == SCISSORS:

        if c == ROCK:
            computer_score += 1
            return f"Computer Win.. Your Score = {user_score} || Computer Score = {computer_score}"
        else:
            user_score += 1
            return f"You Win.. Your Score = {user_score} : Computer Score = {computer_score}"


# Start Game

game_start = int(input("Insert 1. To Playing Game : "))
game_round = 1

if game_start != 1:
    print("Invalid, Game Cannot Start")
else:
    while game_start:

        print(f"----- ROUND {game_round} -----", end="\n")

        user = user_turn()
        print(f"Your Choice ↓↓↓ \n {user}", end='\n')

        computer = computer_turn()
        print(f"Computer Choice ↓↓↓ {computer}", end='\n')

        print(f"Result ::: {result(user, computer)}", end='\n')

        game_round += 1

        continue_game = int(
            input("Insert 1. Continue Game / Insert Any Number to Exit The Game : "))

        if continue_game == 1:
            game_start = 1
        else:
            game_start = 0

print(
    f"Game Over, You Exit The Game... Final Score (You : {user_score}, Computer : {computer_score})")
