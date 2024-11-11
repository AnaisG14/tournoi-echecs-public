from models import tournament, player, lap, match, connexion_db
from controllers import launch_tournament
from tinydb import TinyDB, Query

information_tournament1 = {"tournament_name": "Tournois paris",
                           "tournament_place": "paris",
                           "laps_number": 2,
                           "time_controller": "bullet",
                           "manager_description": "test pour un premier tournois",
                           "start_date": "04/10/2021",
                           "end_date": "05/10/2021",
                           'laps_name': [],
                           'laps': [],
                           'players': [],
                           'results': []
                           }
tournois1 = tournament.Tournament(**information_tournament1)

dict_joueur1 = {"first_name": "Anais",
                "last_name": "Gatard",
                "birthday": "14-05-1977",
                "sexe": "F",
                "ranking": 12,
                }

dict_joueur2 = {"first_name": "Fred",
                "last_name": "Lesire",
                "birthday": "01-06-1969",
                "sexe": "M",
                "ranking": 13,
                }
dict_joueur3 = {"first_name": "Guillaume",
                "last_name": "Esnault",
                "birthday": "01-06-1969",
                "sexe": "M",
                "ranking": 26,
                }
dict_joueur4 = {"first_name": "Jean",
                "last_name": "Dupont",
                "birthday": "01-06-1969",
                "sexe": "M",
                "ranking": 4,
                }
dict_joueur5 = {"first_name": "Paul",
                "last_name": "Demarre",
                "birthday": "12-06-1973",
                "sexe": "M",
                "ranking": 22,
                }
dict_joueur6 = {"first_name": "Christelle",
                "last_name": "Adam",
                "birthday": "29-12-1986",
                "sexe": "F",
                "ranking": 16,
                }
dict_joueur7 = {"first_name": "Laure",
                "last_name": "Laure",
                "birthday": "18-07-2008",
                "sexe": "F",
                "ranking": 15,
                }
dict_joueur8 = {"first_name": "Jérémi",
                "last_name": "Sno",
                "birthday": "07-04-2004",
                "sexe": "M",
                "ranking": 29,
                }
Anais = player.Player(**dict_joueur1)
Fred = player.Player(**dict_joueur2)
Guillaume = player.Player(**dict_joueur3)
Jean = player.Player(**dict_joueur4)
Paul = player.Player(**dict_joueur5)
Christelle = player.Player(**dict_joueur6)
Laure = player.Player(**dict_joueur7)
Jeremi = player.Player(**dict_joueur8)

tournois1.add_players(Anais)
tournois1.add_players(Fred)
tournois1.add_players(Guillaume)
tournois1.add_players(Jean)
tournois1.add_players(Paul)
tournois1.add_players(Christelle)
tournois1.add_players(Laure)
tournois1.add_players(Jeremi)
print(f"ajout d'un joueur {tournois1.players}")

# print("lancement d'un tournoi")
# lancement_tournois = launch_tournament.LaunchTournament(tournois1)
# lancement_tournois()


# lap1 = lap.lap(tournois1)
# print(type(lap1.lap_players))
# print(type(lap1.lap_players[0][0]))
# joueur_1 = lap1.lap_players[0]
# joueur_2 = lap1.lap_players[1]
# match_test = match.Match(joueur_1, joueur_2)
# lap1.add_match(match_test)
# s_lap1 = lap1.serialize()
# print(f"lap1 sérialisé {s_lap1}")
# tournois1.add_laps(lap1)
# s_tournois1 = tournois1.serialize()
# print(s_tournois1)

# tournois1.save()

# tournois2 = tournament.Tournament.get()
# print(tournois2)
# for tournois in tournois2:
#     print(f"nom tournois2: {tournois.tournament_name}")
#     # print(f"joueurs tournois: {tournois.players}")
#     # print(f"laps: {tournois.laps}")
# # tournois2[0].save()
#
# # s_match = match_test.serialize()
# # print(s_match)
#
db = TinyDB('db.json')
tournaments_table = db.table('tournaments')
tournaments_players = db.table('players')

print("modif du rang de Anais")
User = Query
self.players_table.update({'ranking': ranking}), (User.last_name == last_name) and (User.first_name == first_name)


# tournois = tournaments_table.all()
# print(len(tournois))
#
# test = management_tournament.ManagementTournament()
# for tournament in test.all_tournaments:
#     print(type(tournament))
# tournaments_table.truncate()
# tournaments_players.truncate()
# tournaments_table.insert(s_tournois1)
# for each_player in tournois1.players:
#     each_player.save_player()

# deserialized_players = player.PlayerManager.get_all_from_db()
# for deserialized_player in deserialized_players:
#     new_player = player.Player.get(deserialized_player)
#     print(new_player, end="")

# tournois1.save()

# recreate_tournament = tournament.Tournament.get()
# print("\n",recreate_tournament.tournament_name)
# print(recreate_tournament.players)
# # for player in recreate_tournament.players:
# #     print(player.last_name)
#
# print(recreate_tournament.laps)


# tournois2 = tournament.Tournament.get(serialized_tournois1)
# print(f"test réussi: \n {tournois2.tournament_name}")
# print(f"laps: {tournois2.laps}")
# tournois2.save_tournament()
# # app = launch_tournament.LaunchTournament(tournois2)
# # app()

# test = tournament.TournamentManager.get_all_from_db()
# print(type(test))
# for tournament in test:
#     print(f"{type(tournament)}\n")
#     # tournament.TournamentManager.deserialize(test)
#
# db = TinyDB('db.json')
# tournaments_table = db.table('tournaments')
# tournaments_players = db.table('players')

# db = TinyDB('dbtest.json')
# db.truncate()
# anais_s = Anais.serialize()
# db.insert(anais_s)
# serialized_anais = db.all()
# print("\n\n")
# for dict in serialized_anais:
#     print(dict)
#     new_anais = {'first_name': dict['first_name'],
#     'last_name': dict['last_name'],
#     'birthday': dict['birthday'],
#                  'sexe': dict['sexe'],
#     'ranking': dict['ranking']
#     }
# NewAnais = player.Player(**new_anais)
# print(NewAnais.last_name)


