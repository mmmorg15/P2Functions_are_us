# Colby Eastmond
# A4 - Soccer Teams

import random
def menu():
    print("1.Play Simulator\n2.Exit ")
    iChoice=int(input("What would you like to do (1 or 2?)"))
    return iChoice

iDecision=menu()
if iDecision ==1:
else:


# Gather inputs
home = input("Enter the name of your team (home team): ")
teams = int(input(f"Enter the number of teams that {home} will play (1-10): "))

# Initialize dictionary
games_dict = {}

# Initialize wins and losses
wins = 0
losses = 0

# Loop through each of the teams that the home team will play
for i in range(teams):
    # Collect input for the away team
    away = input(f"Enter the name of the away team for game {i + 1}: ")

    # Set scores equal to enter the while loop
    home_score = 0
    away_score = 0

    while home_score == away_score:
        # Randomly calculate scores
        home_score = random.randint(1, 10)
        away_score = random.randint(1, 10)

    # Determine whether the result was a win or loss for the home team
    if home_score > away_score:
        result = "W"
        wins += 1
    else:
        result = "L"
        losses += 1

    # Create a list to store the results
    game_result = [home, home_score, away, away_score]

    # Add to dictionary
    games_dict[i] = game_result


# Print the results
for i in range(len(games_dict)):
    print(f"{games_dict[i][0]}'s score: {games_dict[i][1]}, {games_dict[i][2]}'s score: {games_dict[i][3]}")

print(f"Final season record: {wins} - {losses}")
if wins >= losses:
    print("You had a good season")
else:
    print("Better luck next year")