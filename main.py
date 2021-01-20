import random
import art
from game_data import data
import replit

def getRandomAccount():
    """Geneartes and returns a random account from the data list"""
    return random.choice(data)

def checkAnswer(choice, accountAFollow, accountBFollow):
    """Checks if the user guess is correct or not"""
    if (accountAFollow >= accountBFollow and choice == 'A') or (accountBFollow >= accountAFollow and choice == 'B'):
        return 1
    else:
        return 0

def higherLower():
    """Driver function for the game"""
    global score
    global accountA
    accountB = getRandomAccount()
    while accountB == accountA:
        personB = getRandomAccount()

    print(f"Compare A: {accountA['name']}, a {accountA['description']}, from {accountA['country']}.")
    print(art.vs)
    print(f"Against B: {accountB['name']}, a {accountB['description']}, from {accountB['country']}.")
    choice = input("Who has more folowers? Type 'A' or 'B': ").upper()

    accountAFollow = accountA["follower_count"]
    accountBFollow = accountB["follower_count"]

    replit.clear()
    print(art.logo)
    if checkAnswer(choice, accountAFollow, accountBFollow) == 1:
        score += 1
        print(f"You're right! Current Score = {score}")
        accountA = accountB
        higherLower()
    else:
        print(f"Sorry, thats wrong. Final Score = {score}")
        return

accountA = random.choice(data)
score = 0
print(art.logo)
higherLower()