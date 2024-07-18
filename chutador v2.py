# Esta é uma nova versão do chutador de números, com uma outra forma de fazer. 

import random as r 
import os

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

EASY_MODE = 10
HARD_MODE = 5

def clear():
  """Function used to clear the previus print"""
  os.system('cls' if os.name == 'nt' else 'clear')

def guess_number():
    """Function used to generate a random number in range 1 to 100"""
    number = r.randint(1,100)
    return number

def play_again():
  play_again = input('Do you want to play again? Type \'y\' or \'n\': ')
  if play_again == 'y':
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    return False
  else:
    return True  

def check_number(guess, answer, turns):
    """Function to check if guess number inserted by user is greater or less than a generated random number"""
    if guess > answer:
        print('Too high.')
        return turns - 1
    elif guess < answer:
        print('Too low.')
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")  
        return -1      

def set_dificulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while level not in ['easy', 'hard']:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_MODE
    else:
        return HARD_MODE

      

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = guess_number()
    game_over = False
    while not game_over:
        turns = set_dificulty()
        guess = 0
        while guess != answer:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess = int(input('Make a guess: '))
            turns = check_number(guess, answer, turns)

            if turns == 0:
                print("You've run out of guesses, you lose.")
                game_over = play_again()
                break
            elif turns == -1:
                game_over = play_again()
                break
            elif guess != answer:
                print("Guess again.")

game()