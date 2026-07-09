import pprint
players = {    'Haaland':{ 'name': 'Haaland',    'position': 'St',    'club': 'Man city',   'goals': 15,    'assists': 12},
              'Bellingham':{'name':'Bellingham', 'position': 'Mf', 'club': 'Real Madrid', 'goals': 15, 'assists': 12 },
              'Saka':{'name':'Saka', 'position': 'Rw', 'club': 'Arsenal', 'goals': 9, 'assists': 12 }
              }
print('These are the players and their stats: ')
pprint.pprint(players)
players['Haaland'].update({'goals':'61' , 'assists':'11'})
players.update({'Bellingham': {'position':'Amf' , 'club': 'England'}})
players['Haaland'].pop('club')
print("Any new statistics you'd like to change?")
footballer = input('footballer name:  ')
statistic_name = input('statistic name:  ').lower()
statistic = input('statistic:  ')
players[footballer].update({statistic_name: statistic})
pprint.pprint(players, sort_dicts=False)
