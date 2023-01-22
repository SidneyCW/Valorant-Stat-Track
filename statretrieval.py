import requests
import itertools

# initialize variables used for url
player_name = 'SleepySidney'
tag = 'merp'
game_mode = 'competitive'

# URL for the player statistics endpoint
url = 'https://api.henrikdev.xyz/valorant/v3/matches/na/' + player_name + '/' + tag + '?filter=' + game_mode


# Send a GET request to the URL
response = requests.get(url)

# Check the status code of the response
if response.status_code != 200:
    print('Error: Unable to retrieve player statistics')
    print(response.text)
    exit()

# Load the JSON data from the response
data = response.json()

# Initialize lists for data storage
other_player_kills = []
your_kills = []
your_kills_vs_other = []

# Extract all kills data
for match in data['data']:
    other_player_kills_in_match = []
    for player in match['players']['all_players']:
        kills = player['stats']['kills']
        if player['name'] == player_name:
            your_kills.append(kills)
        else:
            other_player_kills_in_match.append(kills)
    other_player_kills.append(other_player_kills_in_match)

# Create a list with comparison to other players in match
for idx, match in enumerate(other_player_kills):
    match_avg = sum(match)/len(match)
    if your_kills[idx] > match_avg: your_kills_vs_other.append(' ^ ')
    if your_kills[idx] < match_avg: your_kills_vs_other.append(' v ')
    else: your_kills_vs_other.append(' - ')

# Output all important Data
print(other_player_kills)
print(your_kills)
print(your_kills_vs_other)
other_player_kills = list(itertools.chain.from_iterable(other_player_kills))
print('avg other player kills in last 5 games: ',sum(other_player_kills)/len(other_player_kills),'\nyour avg kills in last 5 games: ',sum(your_kills)/len(your_kills))