from ..models import tournament
from ..views import tournament_view

information_tournament = {"tournament_name": "Tournois test",
                          "tournament_place": "Sens",
                          "laps_number": 4,
                          "time_controller": "bullet",
                          "laps_name": ["lap1", "lap2", "lap3"],
                          'start_date': "14-12-2021",
                          'end_date': "14-12-2021",
                          "manager_description": "test pour un premier tournois",
                          }

tournois = tournament.Tournament(**information_tournament)
print(tournois.tournament_name)
print(tournois)


info_tournois = tournament_view.TournamentView()
info_tournois.add_questions("quel est votre nom", "nom")
info_tournois.add_questions("quel est votre age", "age")
info_tournois.ask_questions(info_tournois.questions)
print(info_tournois)
