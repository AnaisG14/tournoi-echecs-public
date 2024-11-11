from operator import attrgetter
from ..views import player_view
from ..controllers import management_tournament, home_menu_controller


class ReportActors(management_tournament.ManagementTournament):
    """ Display a list of all actors, by alphabetical or ranking. """
    def __init__(self, tournament=None, option=""):
        super().__init__()
        self.display_report = player_view.PlayerView()
        self.option = option
        if tournament:
            self.actors = tournament.players
        else:
            self.actors = []

    def __call__(self):
        if not self.option:
            if self.all_players:
                self.actors = self.all_players
                test_reponse = False
                while not test_reponse:
                    response = self.display_report.ask_questions("Selectionnez 1 pour un affichage par ordre "
                                                                 "alphabétique ou 2 pour un affichage par rang: ")
                    if response == "1":
                        self.actors = self.list_actors("name")
                        self.display_report.display_actors(self.actors)
                        test_reponse = True
                        return home_menu_controller.HomeMenuController()
                    elif response == "2":
                        self.actors = self.list_actors()
                        self.display_report.display_actors(self.actors)
                        test_reponse = True
                        return home_menu_controller.HomeMenuController()
                    else:
                        self.display_report.display_informations("Vous devez choisir 1 ou 2")
            else:
                self.display_report.display_informations("\nAucun joeurs dans la base de connées")
                return home_menu_controller.HomeMenuController()
        else:
            test_reponse = False
            while not test_reponse:
                response = self.display_report.ask_questions("Selectionnez 1 pour un affichage par ordre "
                                                             "alphabétique ou 2 pour un affichage par classement: ")
                if response == "1":
                    self.actors = self.list_actors("name")
                    self.display_report.display_actors(self.actors)
                    test_reponse = True
                    return home_menu_controller.HomeMenuController()
                elif response == "2":
                    self.actors = self.list_actors()
                    self.display_report.display_actors(self.actors)
                    test_reponse = True
                    return home_menu_controller.HomeMenuController()
                else:
                    self.display_report.display_informations("Vous devez choisir 1 ou 2")

    def list_actors(self, sort_methode="classement"):
        """ display all the actors of all tournament
        You can sort by name or by score."""

        if sort_methode == "name":
            self.actors.sort(key=attrgetter("last_name"))
            return self.actors
        else:
            self.actors.sort(key=attrgetter("ranking"))
            return self.actors
