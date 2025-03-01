# Colby Eastmond, Merrick Morgan, Spencer Jorgensen, Talon Condie, Jacob Lee
# P2 - Function Are Us
# Created a script to use functions to run simulations of soccer games similar to assignment 4.


import random
# Function 1 - Function to get the user's name (Jacob's function)
def introduction():
    print("\nWelcome to the Soccer Season Simulator! \n")
    sName = input("What is your name? ").capitalize().strip( )
    print(f"Welcome {sName}! Let's get started! \n")
    return sName

# Function 2 - Gather input for whether or not to play
def menu():
    print("1.Play Simulator\n2.Exit ")
    iChoice=int(input("What would you like to do (1 or 2?)"))
    return iChoice

# Creating Function 3 - Using Big 12 teams for the teams list default
def team_selection(team_list = None, n_games = 3):
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

    # Receive user input for which teams will be the away team
    away_team = []
    for i in range(n_games):
        away_index = int(input(f"Please select away team {i + 1} (input the number by the team name): "))
        away_team.append(team_list[away_index - 1])

    return home_team, away_team

# Creates function 4
def play_game( home_team = None, away_team = None, n_games = 3  ):
    wins = 0
    losses = 0

    for i in range(n_games):
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

        # Display the results
        print(f"{home_team} scored {home_score} points, {away_team[i]} scored {away_score} points. This resulted in a {result} for {home_team}.")
    
    #When the function is called it will print the following sentence
    return home_team, wins, losses


def finalRecord(home, wins, losses): 
    print(f"{home} final season record: {wins} - {losses}")
    if wins >= losses:
        print("You had a good season")
    else:
        print("Better luck next year")



# Begin calling functions to run the program
# Gather user name and print welcome statement
introduction()

# Gather input for whether or not to play the game
choice = menu()

# Begin simulation
if choice == 1:
    n_games = int(input("How many games would you like to play (1, 2, 3,...)? "))
    home_team, away_team = team_selection(n_games = n_games)

    home_team, wins, losses = play_game(home_team = home_team, away_team = away_team, n_games = n_games)

    finalRecord(home = home_team, wins = wins, losses = losses)
else:
    print("Exiting the program.")
