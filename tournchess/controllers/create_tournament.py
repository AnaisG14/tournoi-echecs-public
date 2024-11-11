from ..models import tournament
from ..views import tournament_view
from ..controllers import add_players, home_menu_controller
from ..utils import verify_response


class CreateTournament:
    """ Ask questions to the manager. Use these informations to create a tournament. """

    def __init__(self):
        self.new_tournament = None
        self.tournament_view = tournament_view.TournamentView(self.new_tournament)
        self.attribut_tournament = {}

    def __call__(self):
        """ Add questions to the model and ask questions to the user"""
        # add questions to create tournament
        self.tournament_view.add_questions("Donnez un nom au tournois à créer:\n",
                                           "tournament_name",
                                           "required")
        self.tournament_view.add_questions("Indiquez le lieu de votre tournois:\n",
                                           "tournament_place",
                                           "required")
        self.tournament_view.add_questions("Indiquez le nombre de tours (par défaut 4):\n",
                                           "laps_number",
                                           int,
                                           4)
        self.tournament_view.add_questions("Quel sera le contrôleur de temps (bullet, blitz, coup rapide):\n",
                                           "time_controller",
                                           ['bullet', 'blitz', 'coup rapide'])
        self.tournament_view.add_questions("Description du tournois facultatif:\n",
                                           "manager_description")
        self.tournament_view.add_questions("Date de début (dd-mm-aaaa):\n",
                                           "start_date",
                                           "date")
        self.tournament_view.add_questions("Date de fin (dd-mm-aaaa):\n",
                                           "end_date",
                                           "date")

        # ask question to manager
        for question in self.tournament_view.questions:
            self.verification = False
            while not self.verification:
                response = self.tournament_view.ask_questions(question[0])
                if not response:
                    response = question[3]
                test_response = verify_response.verify_response(question, response)
                if test_response:
                    self.verification = True
                    self.attribut_tournament[question[1]] = response
        self.new_tournament = tournament.Tournament(**self.attribut_tournament)
        self.tournament_view = tournament_view.TournamentView(self.new_tournament)
        self.tournament_view.display_responses()
        response = ""
        autorized_response = ["o", "n", "O", "N"]
        while response not in autorized_response:
            response = self.tournament_view.ask_questions("Répondez par o ou n.\n"
                                                          "Souhaitez-vous ajouter vos joueurs maintenant ? (o/n) ")
        if response == "o" or response == "O":
            return add_players.AddPlayers(self.new_tournament)
        else:
            self.new_tournament.save()
            return home_menu_controller.HomeMenuController()
