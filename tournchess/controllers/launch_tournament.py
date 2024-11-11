from ..models import lap, match
from ..views import display_matches, tournament_view
from ..controllers import management_tournament, home_menu_controller, player_ranking
from ..utils import verify_response


class LaunchTournament:
    """ Start the tournament :
        - generate the first lap if it is a new tournament
        - generate the next laps
        For each lap, generation of matches, ask scores to the manager and update the players scores.
        At the end of the lap, the manager can save and quit the tournament.
        """

    def __init__(self, tournament_instance):
        self.tournament_view = tournament_view.TournamentView()
        self.tournament = tournament_instance
        self.laps_view = display_matches.DisplayMatches(self.tournament)
        self.manage_tournament = management_tournament.ManagementTournament()
        self.quitter = False

    def __call__(self):
        self.wait_response("lancer le tour. ")
        while not self.quitter:
            if len(self.tournament.laps) < int(self.tournament.laps_number):
                if not self.tournament.laps:
                    self.generate_first_lap()
                    self.wait_response("lancer le tour suivant. ")
                else:
                    self.generate_laps(f"{self.tournament.laps_name[len(self.tournament.laps)]}")
                    self.wait_response("lancer le tour suivant. ")
            else:
                self.tournament.results = self.tournament.players_scores
                self.laps_view.results = self.tournament.players_scores
                self.laps_view.display_classement()
                self.wait_response("modifier le rang des joueurs du tournoi. ")
                self.tournament.save()
                return player_ranking.PlayerRanking(self.tournament.players)
        return home_menu_controller.HomeMenuController()

    def generate_first_lap(self):
        """ Generate the first matches in function of the player ranking.
        Wait for the scores and update the scores.
        """
        self.tournament.players_scores = [[player, 0] for player in self.tournament.players]
        new_lap = lap.Lap(self.tournament.laps_name[0])
        self.generate_first_pairs(new_lap)
        self.laps_view.display_matches(new_lap.matches)
        self.laps_view.display_information("Entrez les scores pour chaque premier joueur du match")
        new_lap.add_end_time()
        self.add_score(new_lap)
        self.tournament.add_laps(new_lap)

    def add_score(self, lap):
        """ Ask manager to enter score at the end of a match and update the player score. """
        for each_match in lap.matches:
            verification = False
            while not verification:
                score = self.laps_view.ask_question(f"Score de {each_match.opponents[0][0]}")
                test_score = verify_response.check_float(score)
                if test_score:
                    verification = True
                    each_match.modify_score(score)
        self.laps_view.display_score(lap.matches)

    def generate_laps(self, lap_name):
        """ Generate laps after the first lap. """
        new_lap = lap.Lap(lap_name)
        new_lap.matches = []
        self.generate_pairs(new_lap, self.tournament.players_scores)
        self.laps_view.display_matches(new_lap.matches)
        self.laps_view.display_information("Entrez les scores pour chaque premier joueur du match.")
        new_lap.add_end_time()
        self.add_score(new_lap)
        self.tournament.add_laps(new_lap)

    def generate_first_pairs(self, lap):
        """ Generate pairs of players for the first lap in function of their ranking. """
        # classer les joueurs en fonction de leur rang
        list_players_sorted = sorted(self.tournament.players_scores, key=lambda x: x[0].ranking)
        number_of_pairs = len(self.tournament.players_scores)/2
        nb = 0
        while nb < number_of_pairs:
            player1 = list_players_sorted[nb]
            player2 = list_players_sorted[int(nb + number_of_pairs)]
            lap.add_match(match.Match(player1, player2))
            nb += 1

    def generate_pairs(self, lap, players):
        """ Generate pairs of players for one lap in function of their score. """
        # classer les joueurs en fonction de leur score puis de leur rang
        essais = 0
        list_players_sorted = sorted(players,
                                     key=lambda x: (x[1], x[0].ranking))
        while list_players_sorted:
            player1 = list_players_sorted.pop(0)
            player2 = list_players_sorted[0]
            test_pair = self.verify_pairs(player1, player2)
            if test_pair:
                player2 = list_players_sorted.pop(0)
                lap.add_match(match.Match(player1, player2))
            else:
                try:
                    player2 = list_players_sorted.pop(1)
                except IndexError:
                    list_players_sorted = sorted(players, key=lambda x: (x[1], x[0].ranking))
                    if essais == 0:
                        list_players_sorted[1], list_players_sorted[2] = list_players_sorted[2], list_players_sorted[1]
                    if essais == 1:
                        list_players_sorted[2], list_players_sorted[3] = list_players_sorted[3], list_players_sorted[2]
                    if essais == 2:
                        list_players_sorted[3], list_players_sorted[4] = list_players_sorted[4], list_players_sorted[3]
                    if essais == 3:
                        list_players_sorted[1], list_players_sorted[3] = list_players_sorted[3], list_players_sorted[1]
                    if essais == 4:
                        list_players_sorted[2], list_players_sorted[4] = list_players_sorted[4], list_players_sorted[2]
                    if essais == 5:
                        return "Impossible d'associer les joueurs"
                    essais += 1
                    lap.matches.clear()
                else:
                    lap.add_match(match.Match(player1, player2))

    def verify_pairs(self, player1, player2):
        """ Verify that opponents have never play against each other. """
        for each_lap in self.tournament.laps:
            for each_match in each_lap.matches:
                if player1 in each_match.opponents:
                    if player2 in each_match.opponents:
                        return "impossible"
        return True

    def wait_response(self, question):
        """ Ask user if he wants to quit ou continue. """
        response = self.laps_view.ask_question(f"Tapez 'q' pour retourner au menu principal"
                                               f"(votre progression dans le tournoi sera sauvegarder). "
                                               f"Tapez n'importe quelle touche pour {question}")
        if response == "q":
            self.tournament.save()
            self.quitter = True
        else:
            self.quitter = False
