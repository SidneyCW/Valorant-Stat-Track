import requests

def getUrl(player: str,tag: str, mode: str) -> str:
    # URL for the player statistics endpoint
    url = 'https://api.henrikdev.xyz/valorant/v3/matches/na/' + player + '/' + tag + '?filter=' + mode
    return url

def getResponse(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code != 200:
        print('Error: Unable to retrieve player statistics')
        print(response.text)
        exit()
    
    # Load the JSON data from the response
    data = response.json()
    return data


def extractKills(data: str,player_name: str) -> list:

    other_player_kills = []
    your_kills = []

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
    return [your_kills, other_player_kills]

def myComparison(your_kills: list, other_player_kills: list) -> list:
    your_kills_vs_other = []
    # Create a list with comparison to other players in match
    for idx, match in enumerate(other_player_kills):
        match_avg = sum(match)/len(match)

        if your_kills[idx] > match_avg: 
            your_kills_vs_other.append(' ^ ')

        if your_kills[idx] < match_avg: your_kills_vs_other.append(' v ')

        else: your_kills_vs_other.append(' - ')
    return your_kills_vs_other