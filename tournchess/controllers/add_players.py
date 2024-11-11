from ..models import player
from ..views import player_view
from ..controllers import launch_tournament, home_menu_controller
from ..utils import verify_response


class AddPlayers:
    """ Add players in the tournament passed in parameter or in the database if no tournament passed."""

    def __init__(self, tournament=None):
        self.tournament = tournament
        self.view_get_information_player = player_view.PlayerView()
        self.informations_player = {}
        self.verification = False
        self.player_index = 1
        self.number_player_to_add = 8
        self.all_players = player.PlayerManager.get_all()

    def __call__(self):
        if not self.tournament:
            answer = None
            while not answer:
                response = self.view_get_information_player.ask_questions("Combien voulez-vous inscrire "
                                                                          "de personnes ?")
                try:
                    answer = int(response)
                except ValueError:
                    self.view_get_information_player.display_informations("Vous devez entrez un nombre")
                else:
                    self.number_player_to_add = int(response)

        # add questions to the view to create the player
        self.view_get_information_player.add_questions("Nom du joueur:\n", "last_name", "required")
        self.view_get_information_player.add_questions("prénom du joueur:\n", "first_name", "required")
        self.view_get_information_player.add_questions("Date de naisance du joueur (jj-mm-aaaa):\n",
                                                       "birthday", "date")
        self.view_get_information_player.add_questions("Sexe du joueur (M/F):\n", "sexe", ['M', 'F'])
        self.view_get_information_player.add_questions("Rang du joueur:\n", "ranking", int)

        number_player_save = 1
        while self.number_player_to_add:
            # ask question to manager
            self.view_get_information_player.display_informations(
                f"Entrez les informations du joueur"
                f"{self.number_player_to_add - (self.number_player_to_add - number_player_save)}")
            number_player_save += 1
            self.add_player_index()
            for question in self.view_get_information_player.questions:
                self.verification = False
                while not self.verification:
                    response = self.view_get_information_player.ask_questions(question[0])
                    test_response = verify_response.verify_response(question, response)
                    if test_response:
                        self.verification = True
                        self.informations_player[question[1]] = response
            new_player = player.Player(**self.informations_player)
            self.test_new_player(new_player)
            if self.tournament:
                self.tournament.add_players(new_player)

            self.number_player_to_add -= 1
            self.view_get_information_player.display_informations("Le joueur a été ajouté.")
        if self.tournament:
            self.view_get_information_player.display_informations("Tous les joueurs ont été ajoutés.")
            return launch_tournament.LaunchTournament(self.tournament)
        else:
            return home_menu_controller.HomeMenuController()

    def add_player_index(self):
        """ Add an index for each player added. """
        self.view_get_information_player.responses["index"] = self.player_index
        self.player_index += 1

    def test_new_player(self, new_player):
        """ Verification if the player exists in the database. If the player exists, modification of
        his ranking."""
        last_names_players = []
        first_names_players = []
        birthday_players = []
        for item in self.all_players:
            last_names_players.append(item.last_name)
            first_names_players.append(item.first_name)
            birthday_players.append(item.birthday)
        if new_player.last_name in last_names_players and new_player.first_name in first_names_players and \
                new_player.birthday in birthday_players:
            new_player.modify_ranking(new_player.ranking)
        else:
            new_player.save()
