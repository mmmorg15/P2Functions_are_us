# Spencer Jorgensen
# 2/28/2025
# This creates a function that takes a home team and an away team and generates a random score for each of them. It then prints off the scores and if the home team won or loss

import random

# Creates the function
def play_game( home_team = None, away_team = None   ):
    
    # Set scores equal to enter the while loop
    home_score = 0
    away_score = 0

    while home_score == away_score:
        # Randomly calculate scores
        home_score = random.randint(1, 10)
        away_score = random.randint(1, 10)

    # Initialize wins and losses
    wins = 0
    losses = 0

    # Determine whether the result was a win or loss for the home team
    if home_score > away_score:
        result = "W"
        wins += 1
    else:
        result = "L"
        losses += 1
    # Create a list to store the results
    game_result = [home_team, home_score, away_team, away_score]
    
    #When the function is called it will print the following sentence
    return print(f"{home_team} scored {home_score} points, {away_team} scored {away_score} points. This resulted in a {result} for {home_team}.")
