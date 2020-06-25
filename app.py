import constants
import random

TEAMS = constants.TEAMS
PLAYER_DATA = constants.PLAYERS

players = PLAYER_DATA
num_players_team = len(PLAYER_DATA) / len(TEAMS)
panthers = { 'name': 'Panthers', 'players': [],}
bandits = { 'name': 'Bandits', 'players': [],}
warriors = { 'name': 'Warriors', 'players': [],}
experienced_players = []
inexperienced_players = []

def clean_data(data):
    for player in data:
        player['height'] = int(player['height'][0:2])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player['guardians'] = player['guardians'].split(' and ')
    return data

def balance_teams(team_a, team_b, team_c):
    while len(team_a['players']) < num_players_team:
        team_a['players'].append(experienced_players.pop(random.randint(0, len(experienced_players) - 1)))
        team_a['players'].append(inexperienced_players.pop(random.randint(0, len(inexperienced_players) - 1)))
    while len(team_b['players']) < num_players_team:
        team_b['players'].append(experienced_players.pop(random.randint(0, len(experienced_players) - 1)))
        team_b['players'].append(inexperienced_players.pop(random.randint(0, len(inexperienced_players) - 1)))
    while len(team_c['players']) < num_players_team:
        team_c['players'].append(experienced_players.pop(random.randint(0, len(experienced_players) - 1)))
        team_c['players'].append(inexperienced_players.pop(random.randint(0, len(inexperienced_players) - 1)))

def main_menu():
    print("""\nBASKETBALL STATS TOOL
    
---- MENU ----


Select an option:
  1) Display Team Stats
  2) Quit
""")
    choice = input("")
    while True:
        if choice == '1':
            team_menu()
        elif choice == '2':
            exit()
        else:
            choice = input("Please select a valid choice.  ")
    

def team_menu():
    print("""\nSelect an option:
  1) Panthers
  2) Bandits
  3) Warriors""")
    choice = input("")
    while True:
        if choice == '1':
            display_team_stats(panthers)
            break
        elif choice == '2':
            display_team_stats(bandits)
            break
        elif choice == '3':
            display_team_stats(warriors)
            break
        else:
            choice = input("Please select a valid choice.  ")
    cont = input("Would you like to continue? (yes/no) ")
    if cont.lower() == 'yes':
        main_menu()
    else:
        exit()


def display_team_stats(team):
    print(f"\nTeam: {team['name']} Stats")
    print("-" * 21, "\n")
    print(f"Total players: {len(team['players'])}")
    exp = []
    inexp = []
    for player in team['players']:
        if player.get('experience') == True:
            exp.append(player)
        else:
            inexp.append(player)
    print(f"Total experienced: {len(exp)}")
    print(f"Total inexperienced: {len(inexp)}")
    print(f"Average height: {team.get('average height')}\n")
    team_players = []
    for player in team['players']:
        team_players.append(player.get('name'))
    print(f"{team['name']} Players:")
    print("-"*18)
    all_players = ", ".join(team_players)
    print(f"{all_players}\n")
    print("Player Guardians:")
    print("-"*18)
    guardians = []
    for player in team['players']:
        guardians += player.get('guardians')
    all_guardians = ", ".join(guardians)
    print(f"{all_guardians}\n")
    

def calc_team_height(team):
    total_height = 0
    for player in team['players']:
        total_height += player.get('height')
    return total_height / num_players_team

def round_num(num, decimals=0):
    multipler = 10 ** decimals
    return int(num * multipler) / multipler



if __name__ == '__main__':    

    players = clean_data(players)

    for player in players:
        if player['experience']:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)

    balance_teams(panthers, bandits, warriors)

    panthers['average height'] = round_num(calc_team_height(panthers), 1)
    bandits['average height'] = round_num(calc_team_height(bandits), 1)
    warriors['average height'] = round_num(calc_team_height(warriors), 1)
    
    main_menu()