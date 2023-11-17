import statretrieval

player_name = input('Enter Valorant Name: ')
tag = input('Enter Valorant tag: ')
mode = input('Enter the desired mode: ')

url = statretrieval.getUrl(player_name,tag,mode)
data = statretrieval.getResponse(url)
your_kills = statretrieval.extractKills(data,player_name)[0]
other_player_kills = statretrieval.extractKills(data,player_name)[1]
your_kills_v_others = statretrieval.myComparison(your_kills,other_player_kills)
print(f'Your kills: \n{your_kills}\nOther players kills: \n{other_player_kills}\nYour kills vs others: \n{your_kills_v_others}')