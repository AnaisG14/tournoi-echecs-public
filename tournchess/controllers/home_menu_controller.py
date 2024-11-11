from ..models import home_menu
from ..views import home_menu_view
from ..controllers import create_tournament, add_players, report_actors, report_tournaments, management_tournament, \
    player_ranking


class HomeMenuController:
    """ Add items in the home menu and return the controller corresponding to the user choice."""
    def __init__(self):
        self.home_menu = home_menu.HomeMenu()
        self.menu_view = home_menu_view.HomeMenuView(self.home_menu)

    def __call__(self):
        self.home_menu.add_item("auto", "Créer un tournoi", create_tournament.CreateTournament())
        self.home_menu.add_item("auto", "Poursuivre un tournoi sauvegardé",
                                management_tournament.ManagementTournament())
        self.home_menu.add_item("auto", "Gérer les joueurs", SubMenuPlayer())
        self.home_menu.add_item("auto", "Afficher les rapports", SubMenuTournament())
        self.home_menu.add_item("auto", "Quitter")
        return self.menu_view.user_choice()


class SubMenuPlayer(HomeMenuController):
    """ Add items in the submenu and return the controller corresponding to the user choice."""
    def __init__(self):
        super().__init__()
        self.sub_menu_player = home_menu.HomeMenu()
        self.sub_menu_view = home_menu_view.HomeMenuView(self.sub_menu_player)

    def __call__(self):
        self.sub_menu_player.add_item("auto", "Ajouter des joueurs", add_players.AddPlayers())
        self.sub_menu_player.add_item("auto", "Afficher la liste des joueurs", report_actors.ReportActors())
        self.sub_menu_player.add_item("auto", "Modifier le rang d'un joueur", player_ranking.PlayerRanking())
        self.sub_menu_player.add_item("auto", "Retour au menu principal", HomeMenuController())
        return self.sub_menu_view.user_choice()


class SubMenuTournament(HomeMenuController):
    """ Add choice for the user and ask choice."""

    def __init__(self):
        super().__init__()
        self.sub_menu_tournament = home_menu.HomeMenu()
        self.sub_menu_view = home_menu_view.HomeMenuView(self.sub_menu_tournament)

    def __call__(self):
        self.sub_menu_tournament.add_item("auto", "Afficher la liste des tournois",
                                          report_tournaments.ReportTournament())
        self.sub_menu_tournament.add_item("auto", "Afficher la liste des joueurs d'un tournoi",
                                          report_tournaments.ReportTournament("players"))
        self.sub_menu_tournament.add_item("auto", "Afficher la liste des tours d'un tournoi",
                                          report_tournaments.ReportTournament("laps"))
        self.sub_menu_tournament.add_item("auto", "Afficher la liste des matches d'un tournoi",
                                          report_tournaments.ReportTournament("matches"))
        self.sub_menu_tournament.add_item("auto", "Retour au menu principal", HomeMenuController())
        return self.sub_menu_view.user_choice()
