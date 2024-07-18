import random
import os
from art import logo

def clear():
    """Function used to clear the previus print"""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_cards():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_cards(user_score, computer_score):
    """Function that compares the computer's and user's cards to see who won the game."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You loose 😤"
        

def play_game():
    print(logo)
    c_cards = []
    u_cards = []
    is_game_over = False

    for i in range(2):
        c_cards.append(deal_cards())
        u_cards.append(deal_cards())

    while not is_game_over:
        c_score = calculate_score(c_cards)
        u_score = calculate_score(u_cards)
        print(f"Your cards: {u_cards}, current score: {u_score}")
        print(f"Computer's first card: {c_cards[0]}")

        if u_score == 0 or c_score == 0 or u_score > 21:
            is_game_over = True
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            while get_another_card not in ['y','n']:
                get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if get_another_card == 'y':
                u_cards.append(deal_cards())
            else:
                is_game_over = True

    while c_score != 0 and c_score < 17:
        c_cards.append(deal_cards())
        c_score = calculate_score(c_cards)

    print(f"Your final hand: {u_cards}, final score: {u_score}")
    print(f"Computer's final hand: {c_cards}, final score: {c_score}")
    print(compare_cards(u_score, c_score))

while input("Do you want to play Blackjack? Type 'y' to play and 'n' to leave: ") == 'y':
    clear()
    play_game()