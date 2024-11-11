from models import tournament, player,\
    lap, match, report

# test tournament
information_tournament1 = {"tournament_name": "Tournois test",
                          "tournament_place": "Sens",
                          "laps_number": 4,
                          "time_controller": "bullet",
                          "manager_description": "test pour un premier tournois",
                          "start_date": "04/10/2021",
                           "end_date": "05/10/2021"
                          }
information_tournament2 = {"tournament_name": "Autre tournois test",
                          "tournament_place": "Paris",
                          "laps_number": 3,
                          "time_controller": "blizt",
                          "manager_description": "deuxième tournoi",
                          "start_date": "04/11/2021",
                           "end_date": "05/11/2021"
                          }
print("creation de 2 tournois et d'une liste de tournoi")
tournois1 = tournament.Tournament(**information_tournament1)
tournois2 = tournament.Tournament(**information_tournament2)
print("affichage du nom premier tournoi")
print(tournois1.tournament_name)
print("affichage du 2nd tournoi")
print(tournois2)

# test player et list_player
dict_joueur1 = {"first_name" : "Anais",
                "last_name" : "Gatard",
                "birthday" : "14-05-1977",
                "sexe" : "F",
                "ranking" : 12
                }

dict_joueur2 = {"first_name" : "Fred",
                "last_name" : "Lesire",
                "birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 13
                }
dict_joueur3 = {"first_name" : "Guillaume",
                "last_name" : "Esnault",
                "birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 26
                }
dict_joueur4 = {"first_name" : "Jean",
                "last_name" : "Dupont",
                "birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 4
                }
dict_joueur5 = {"first_name" : "Paul",
                "last_name" : "Demarre",
                "birthday" : "12-06-1973",
                "sexe" : "M",
                "ranking" : 22
                }
dict_joueur6 = {"first_name" : "Christelle",
                "last_name" : "Adam",
                "birthday" : "29-12-1986",
                "sexe" : "F",
                "ranking" : 16
                }
dict_joueur7 = {"first_name" : "Laure",
                "last_name" : "Laure",
                "birthday" : "18-07-2008",
                "sexe" : "F",
                "ranking" : 15
                }
dict_joueur8 = {"first_name" : "Jérémi",
                "last_name" : "Sno",
                "birthday" : "07-04-2004",
                "sexe" : "M",
                "ranking" : 29
                }
Anais = player.Player(**dict_joueur1)
Fred = player.Player(**dict_joueur2)
Guillaume = player.Player(**dict_joueur3)
Jean = player.Player(**dict_joueur4)
Paul = player.Player(**dict_joueur5)
Christelle = player.Player(**dict_joueur6)
Laure = player.Player(**dict_joueur7)
Jeremi = player.Player(**dict_joueur8)
print("affichage des joueurs")
print(Anais)
print(Fred)
print("modification du rang d'un joueur")
Fred.modify_ranking(11)
print(Fred.ranking)
print("ajout des joueurs au tournoi1")
tournois1.add_players(Anais)
tournois1.add_players(Fred)
tournois1.add_players(Guillaume)
tournois1.add_players(Jean)
tournois1.add_players(Paul)
tournois1.add_players(Christelle)
tournois1.add_players(Laure)
tournois1.add_players(Jeremi)
for player in tournois1.players:
    print(player)

print("ajout des joueurs au tournoi2")
tournois2.add_players(Anais)
for player in tournois2.players:
    print(player)

print("créer un lap")
lap1 = lap.lap(tournois1, "lap1")
tournois1.add_laps(lap1)
for player in lap1.lap_players:
    print(player)

print("creation des matches")
lap1.generate_first_pairs()
print(lap1)

print("enregistrement des scores")
print(f"Dupont gagne contre Adam")
Jean.modify_score(Jean.score + 1)
print(f"le nouveau score de Jean est {Jean.score}")
print(f"Demarre gagne contre Gatard")
Paul.modify_score(Paul.score + 1)
print(f"Lesire fait nul contre Esnault")
Fred.modify_score(Fred.score + 0.5)
Guillaume.modifiy_score(Guillaume.score + 0.5)
print(f"Sno gagne contre Laure")
Jeremi.modify_score(Jeremi.score + 1)
lap1.add_end_time()
print(f"lap1 terminé à {lap1.datetime_end}")
print("nouveau lap")
lap2 = lap.lap(tournois1,"lap2")
tournois1.add_laps(lap2)
print("relance des matches")
lap2.generate_pairs()
print(lap2.matches)

print("tournois1")
print(tournois1)
print("classement")
results = tournois1.display_results()
print(results)

# test rapports
rapport1 = report.Report()
rapport1.add_tournament(tournois1)
rapport1.add_tournament(tournois2)
rapport1.list_actors("name")
print(f"Affichage par nom:\n{rapport1.actors}")
rapport1.list_actors("score")
print(f"Affichage par score:\n{rapport1.actors}")
print(f"liste des joueurs du tounois1 par nom")
list_player = rapport1.list_players(tournois1, "name")
for player in list_player:
    print(player)
print(f"liste des joueurs du tounois1 par score")
list_player = rapport1.list_players(tournois1, "score")
for player in list_player:
    print(player)
print(f"liste des tournois")
list_tournament = rapport1.list_tournament()
for tournament in list_tournament:
    print(tournament)
print(f"liste des laps du tournois1")
laps = rapport1.list_laps(tournois1)
for lap in laps:
    print(lap)
print(f"liste des matches du tournois1")
matches = rapport1.list_matches(tournois1)
for match in matches:
    print(match)



