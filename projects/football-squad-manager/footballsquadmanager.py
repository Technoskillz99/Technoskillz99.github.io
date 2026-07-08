players = [
            'Burn',
            'Pickford',
            'Henderson',
            'James',
            'Konsa',
            'Gordon',
            'Morgan',
            'Rogers',
            'Eze',
            'Bellingham',
            'Madueke',
            'Harry',
            'Kane', 
            'Watkins', 
            'Toney']
print(players)
players.append('Stones')
players.remove('Madueke')
players[7] ='Quansah'
print('Add player')
new_player = input()
players.append(new_player)
players.sort()
for player in players:
    print(player)
print("The amount of players in the squad is: " , len(player))
