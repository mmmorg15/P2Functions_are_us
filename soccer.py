# Colby Eastmond
# A4 - Soccer Teams

def finalRecord(home, games): 
    wins = 0
    losses = 0
    for home_score,away_score in games:
        if home_score > away_score:
                wins += 1
        else:
                losses += 1

    print(f"Final season record: {wins} - {losses}")
    if wins >= losses:
        print("You had a good season")
    else:
        print("Better luck next year")


import random
# add a function to get the user's name (Jacob's function)
def introduction():
    print("\nWelcome to the Soccer Season Simulator! \n")
    sName = input("What is your name? ").capitalize().strip( )
    print(f"Welcome {sName}! Let's get started! \n")
    return sName

def menu():
    print("1.Play Simulator\n2.Exit ")
    iChoice=int(input("What would you like to do (1 or 2?)"))
    return iChoice

# Creating Function 3 - Using Big 12 teams for the teams list default
def team_selection(team_list = None):
    # If the user does not input a team list, default to the Big 12 teams
    if team_list == None:
        team_list = ['Arizona', 'Arizona State', 'Baylor', 'Brigham Young', 'Central Florida',
                     'Colorado', 'Houston', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma State',
                     'Texas Christian', 'Texas Tech', 'Utah', 'West Virginia']
        
    # Display the list of teams
    print('Here is the list of teams: ')
    for i in range(len(team_list)):
        print(f'{i + 1}. {team_list[i]}')

    # Receive user input for which team will be the home team
    home_index = int(input("Please select the home team (input the number by the team name): "))

    # Remove that team, assign it to the home_team variable
    home_team = team_list.pop(home_index - 1)

    # Display the list of remaining teams
    print("Here are potential opponents: ")
    for i in range(len(team_list)):
        print(f'{i + 1}. {team_list[i]}')

    # Receive user input for which team will be the away team
    away_index = int(input("Please select the away team (input the number by the team name): "))

    # Assign away team to the away_team variable
    away_team = team_list[i - 1]

    return home_team, away_team

# Creates function 4
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