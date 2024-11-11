from ..models import tournament, player
from ..views import home_menu_view
from ..controllers import launch_tournament, add_players, home_menu_controller


class ManagementTournament:
    """ Get informations of tournaments and players in the database and recreate objects of
    tournament class and player class.
    """

    def __init__(self):
        self.all_tournaments = tournament.TournamentManager.get_all()
        self.all_players = player.PlayerManager.get_all()
        self.menu_tournament_view = home_menu_view.TournamentList
        self.key = 1

    def selecte_tournament(self):
        """ Put in a list all the instance of tournaments. """
        if self.all_tournaments:
            tournament_entries = {}
            keys = []
            for each_tournament in self.all_tournaments:
                tournament_entries[self.key] = each_tournament
                keys.append(self.key)
                self.key += 1
            response = ""
            while response not in keys:
                response = self.menu_tournament_view.choice_tournament(tournament_entries)
                try:
                    response = int(response)
                except ValueError:
                    self.menu_tournament_view.display_informations("Vous devez entrer un nombre")
                else:
                    return tournament_entries[response]
        else:
            return False

    def get_tournament_in_progress(self):
        """ Get in a list all the instances of tournaments in progress. """
        if self.all_tournaments:
            tournament_in_progress = {}
            keys = []
            key = 1
            for each_tournament in self.all_tournaments:
                if not each_tournament.results:
                    tournament_in_progress[key] = each_tournament
                    keys.append(key)
                    key += 1
            if tournament_in_progress:
                response = ""
                while response not in keys:
                    response = self.menu_tournament_view.choice_tournament_in_progress(tournament_in_progress)
                    try:
                        response = int(response)
                    except ValueError:
                        self.menu_tournament_view.display_informations("Vous devez entrer un nombre")
                    else:
                        tournament_get = tournament_in_progress.pop(response)
                        self.all_tournaments = [value for value in tournament_in_progress.values()]
                        tournament.TournamentManager.save_all(self.all_tournaments)
                        return tournament_get
            else:
                self.menu_tournament_view.display_informations("\nAucun tournoi à poursuivre.")
        else:
            self.menu_tournament_view.display_informations("\nAucun tournoi à poursuivre.")
            return False

    def __call__(self):
        tournament_in_progress = self.get_tournament_in_progress()
        if tournament_in_progress:
            if tournament_in_progress.players:
                return launch_tournament.LaunchTournament(tournament_in_progress)
            else:
                return add_players.AddPlayers(tournament_in_progress)
        else:
            return home_menu_controller.HomeMenuController()
