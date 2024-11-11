from ..models import connexion_db
from ..controllers import management_tournament, home_menu_controller
from ..views import player_view


class PlayerRanking:
    """ Modify the ranking of a player after a tournoment or during it. """

    def __init__(self, finish_tournament=None):
        self.managedb = connexion_db.ManagementDB()
        self.get_players = management_tournament.ManagementTournament()
        self.all_players = self.get_players.all_players
        self.player_view = player_view.PlayerView()
        self.players_in_tournament = finish_tournament

    def __call__(self):
        if self.players_in_tournament:
            for each_player in self.players_in_tournament:
                test_response = False
                while not test_response:
                    new_ranking = self.player_view.ask_questions(f"Entrez le nouveau rang de "
                                                                 f"{each_player.first_name} {each_player.last_name}: ")
                    test_response = self.test_ranking(new_ranking)
                    if test_response:
                        each_player.modify_ranking(int(new_ranking))
            self.player_view.display_informations("Les rangs ont été modifiés avec succès")
            return home_menu_controller.HomeMenuController()
        else:
            all_players = {}
            key = 1
            keys = []
            for each_player in self.all_players:
                all_players[key] = each_player
                keys.append(key)
                key += 1
            self.player_view.display_choice_actors(all_players)
            test_choice = False
            while not test_choice:
                index_player = self.player_view.ask_questions("Entrez le numéro du joueur "
                                                              "pour lequel vous souhaitez modifier le rang: ")
                try:
                    int(index_player)
                except ValueError:
                    self.player_view.display_informations("Vous devez entrer un nombre")
                else:
                    if int(index_player) in keys:
                        choosed_player = all_players[int(index_player)]
                        test_response = False
                        while not test_response:
                            new_ranking = self.player_view.ask_questions(f"Entrez le nouveau rang "
                                                                         f"de {choosed_player}: ")
                            test_response = self.test_ranking(new_ranking)
                            if test_response:
                                choosed_player.modify_ranking(int(new_ranking))
                                test_choice = True
                                self.player_view.display_informations("Rang modifié avec succès.")
                    else:
                        self.player_view.display_informations("Vous devez entrer un nombre positif")
        return home_menu_controller.HomeMenuController()

    def test_ranking(self, ranking):
        """ Test if ranking is type int and a positive number. """
        try:
            int(ranking)
        except ValueError:
            self.player_view.display_informations("Vous devez entrer un nombre")
            return False
        else:
            if int(ranking) < 0:
                self.player_view.display_informations("Vous devez entrer un nombre positif.")
                return False
            else:
                return True
