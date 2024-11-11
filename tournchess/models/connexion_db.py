from tinydb import TinyDB, Query


class ManagementDB:
    """ to create, save or get on tiny_db"""
    def __init__(self):
        self.db = TinyDB('db.json')
        self.tournaments_table = self.db.table('tournaments')
        self.players_table = self.db.table('players')

    def get(self, table):
        """ Get all informations in database (players and tournaments). """
        if table == "tournaments":
            return self.tournaments_table.all()
        elif table == "players":
            return self.players_table.all()

    def save(self, table, to_save):
        """ Save players or tournaments in the database. """
        if table == "tournaments":
            self.tournaments_table.insert(to_save)
        elif table == "players":
            self.players_table.insert(to_save)

    def clear_tournaments(self):
        """ Clear the table of tournaments in the database. """
        self.tournaments_table.truncate()

    def modifiy_player_ranking(self, last_name, first_name, birthday, ranking):
        """ Modify the ranking of the player in the database."""
        user = Query()
        self.players_table.update({'ranking': ranking}, (user.last_name == last_name) and
                                  (user.first_name == first_name) and (user.birthday == birthday))
