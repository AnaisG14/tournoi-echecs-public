from .lap import Lap
from .player import Player
from .connexion_db import ManagementDB


class TournamentManager:
    """ serialize and deserialize players and save them into a tinyDB"""
    manage_db = ManagementDB()

    @classmethod
    def deserialize(cls, serialized_tournament):
        """ Desialize a tournament. """
        tournament_name = serialized_tournament['tournament_name']
        tournament_place = serialized_tournament['tournament_place']
        laps_number = serialized_tournament['laps_number']
        time_controller = serialized_tournament['time_controller']
        manager_description = serialized_tournament['manager_description']
        start_date = serialized_tournament['start_date']
        end_date = serialized_tournament['end_date']
        laps_name = serialized_tournament['laps_name']
        laps = []
        deserialized_laps = serialized_tournament['laps']
        deserialized_results = serialized_tournament['results']
        for serialized_lap in deserialized_laps:
            laps.append(Lap.get(serialized_lap))
        players = []
        deserialized_players = serialized_tournament['players']
        for serialized_player in deserialized_players:
            players.append(Player.get(serialized_player))
        players_scores = []
        deserialized_player_score = serialized_tournament['players_scores']
        for serialized_player_score in deserialized_player_score:
            players_scores.append([Player.get(serialized_player_score[0]), serialized_player_score[1]])
        results = []
        for serialilized_result in deserialized_results:
            result_player = [Player.get(
                serialilized_result[0]), serialilized_result[1]]
            results.append(result_player)
        informations_to_create_tournament = {'tournament_name': tournament_name,
                                             'tournament_place': tournament_place,
                                             'laps_number': laps_number,
                                             'time_controller': time_controller,
                                             'manager_description': manager_description,
                                             'start_date': start_date,
                                             'end_date': end_date,
                                             'laps_name': laps_name,
                                             'laps': laps,
                                             'players': players,
                                             'players_scores': players_scores,
                                             'results': results
                                             }
        return informations_to_create_tournament

    @classmethod
    def get_all(cls):
        """ Get all tournaments in database, create an instance of them and add them in a list. """
        all_tournaments = []
        results_db = cls.manage_db.get('tournaments')
        for result in results_db:
            deserialized_tournament = cls.deserialize(result)
            all_tournaments.append(Tournament(**deserialized_tournament))
        return all_tournaments

    @classmethod
    def get_one(cls, serialized_tournament):
        """ Create an instance of a serialided tournament. """
        deserialized_tournament = cls.deserialize(serialized_tournament)
        return Tournament(**deserialized_tournament)

    @classmethod
    def save_all(cls, tournaments):
        """ Save all the tournaments in the database. """
        cls.manage_db.clear_tournaments()
        for tournament in tournaments:
            cls.manage_db.save('tournaments', tournament.serialize())

    @classmethod
    def save_one(cls, serialized_tournament):
        """ Save a tournament in the database. """
        cls.manage_db.save('tournaments', serialized_tournament)


class Tournament:
    """ Model of tournament"""
    manager = TournamentManager()

    def __init__(self, tournament_name, tournament_place, laps_number, time_controller,
                 manager_description, start_date, end_date, laps_name=None, laps=None,
                 players=None, players_scores=None, results=None):
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.laps_number = laps_number
        self.time_controller = time_controller
        self.manager_description = manager_description
        self.start_date = start_date
        self.end_date = end_date
        if laps_name:
            self.laps_name = laps_name
        else:
            self.laps_name = [f"lap {nb+1}" for nb in range(int(laps_number))]
        if laps:
            self.laps = laps
        else:
            self.laps = []
        if players:
            self.players = players
        else:
            self.players = []
        if players_scores:
            self.players_scores = players_scores
        else:
            self.players_scores = []
        if results:
            self.results = results
        else:
            self.results = []
        self.date = (start_date, end_date)

        self.serialized_start_date = f"{self.start_date}"
        self.serialized_end_date = f"{self.end_date}"
        self.serialized_laps = []
        self.serialized_players = []
        self.serialized_players_scores = []
        self.serialized_results = []

    def create_laps_name(self):
        """ Create all the laps of the tournament in function of the number of laps. """
        nb = 1
        laps_number = self.laps_number
        while laps_number:
            self.laps_name.append(f"Lap {nb}")
            nb += 1
            laps_number -= 1

    def display_results(self):
        """ Sort the results of the tournament. """
        print("le tournoi est terminé")
        self.results.sort(key=lambda x: x[1], reverse=True)
        return self.results

    def __str__(self):
        display_tournament = f"Nom du tournoi :{self.tournament_name}\n laps\n"
        for each_lap in self.laps_name:
            display_tournament += f"{each_lap}; "
        display_tournament += "Joueurs\n"
        for each_player in self.players:
            display_tournament += f"{each_player}; "
        return display_tournament

    def __repr__(self):
        display_tournament = f"Nom du tournoi :{self.tournament_name}\n laps\n"
        for each_lap in self.laps_name:
            display_tournament += f"{each_lap}; "
        display_tournament += "Joueurs\n"
        for each_player in self.players:
            display_tournament += f"{each_player}; "
        return display_tournament

    def add_players(self, player):
        """ Add a new player in the tournament. """
        self.players.append(player)

    def add_laps(self, lap):
        """ Add a new lap in the tournament. """
        self.laps.append(lap)

    def serialize(self):
        """ Serialize the tournament in order to save it. """
        for each_lap in self.laps:
            serialized_lap = each_lap.serialize()
            self.serialized_laps.append(serialized_lap)
        for each_player in self.players:
            serialized_player = each_player.serialize()
            self.serialized_players.append(serialized_player)
        for each_player in self.players_scores:
            serialized_player1 = each_player[0].serialize()
            self.serialized_players_scores.append([serialized_player1, each_player[1]])
        for each_result in self.results:
            serialized_result = each_result[0].serialize()
            self.serialized_results.append([serialized_result, each_result[1]])
        serialized_tournament = {
            'tournament_name': self.tournament_name,
            'tournament_place': self.tournament_place,
            'laps_number': self.laps_number,
            'time_controller': self.time_controller,
            'manager_description': self.manager_description,
            'start_date': self.serialized_start_date,
            'end_date': self.serialized_end_date,
            'laps_name': self.laps_name,
            'laps': self.serialized_laps,
            'players': self.serialized_players,
            'players_scores': self.serialized_players_scores,
            'results': self.serialized_results
        }
        return serialized_tournament

    def save(self):
        """ Save the tournament in the database."""
        self.manager.save_one(self.serialize())

    @classmethod
    def get_one(cls, serialized_tournament):
        """ Create an instance of a serialized tournament. """
        return cls.manager.get_one(serialized_tournament)
