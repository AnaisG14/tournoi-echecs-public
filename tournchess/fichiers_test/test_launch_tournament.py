from controllers import launch_tournament
from models import tournament, player


information_tournament1 = {"tournament_name": "Tournois test",
                          "tournament_place": "Sens",
                          "laps_number": 4,
                          "time_controller": "bullet",
                          "manager_description": "test pour un premier tournois",
                          "start_date": "04/10/2021",
                           "end_date": "05/10/2021"
                          }
tournois1 = tournament.Tournament(**information_tournament1)

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

tournois1.add_players(Anais)
tournois1.add_players(Fred)
tournois1.add_players(Guillaume)
tournois1.add_players(Jean)
tournois1.add_players(Paul)
tournois1.add_players(Christelle)
tournois1.add_players(Laure)
tournois1.add_players(Jeremi)

app = launch_tournament.LaunchTournament(tournois1)
app()
