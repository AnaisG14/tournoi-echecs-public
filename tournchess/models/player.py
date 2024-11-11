from .connexion_db import ManagementDB


class PlayerManager:
    """ serialize and deserialize players and save them into a tinyDB"""
    manage_db = ManagementDB()

    @classmethod
    def deserialize(cls, serialized_player):
        """ deserialize method"""
        first_name = serialized_player['first_name']
        last_name = serialized_player['last_name']
        birthday = serialized_player['birthday']
        sexe = serialized_player['sexe']
        ranking = serialized_player['ranking']
        return {'first_name': first_name, 'last_name': last_name,
                'birthday': birthday, 'sexe': sexe,
                'ranking': ranking}

    @classmethod
    def get_all(cls):
        """ Get all players in database and create an instance of each one and stock them in a list. """
        all_players = []
        results_db = cls.manage_db.get('players')
        for result in results_db:
            deserialized_player = cls.deserialize(result)
            all_players.append(Player(**deserialized_player))
        return all_players

    @classmethod
    def get_one(cls, serialized_player):
        """ Create an instance of one player with serialized player data. """
        deserialized_player = cls.deserialize(serialized_player)
        return Player(**deserialized_player)

    @classmethod
    def save_all(cls, players):
        """ Save all players in the database. """
        for each_player in players:
            cls.manage_db.save('players', each_player.serialize())

    @classmethod
    def save_one(cls, serialized_player):
        """ Save one player in the database. """
        cls.manage_db.save('players', serialized_player)


class Player:
    """ Creation of player """
    manager = PlayerManager()

    def __init__(self, first_name, last_name, birthday, sexe, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sexe = sexe
        self.ranking = int(ranking)
        self.tournaments_participation = []

    def modify_ranking(self, new_ranking):
        """ Modify the ranking of a player. """
        self.manager.manage_db.modifiy_player_ranking(self.last_name, self.first_name, self.birthday, new_ranking)

    def add_tournament(self, tournament_name):
        """ Add a player to a tournament. """
        self.tournaments_participation.append(tournament_name)

    def serialize(self):
        """ Serialize player in order to save it. """
        serialized_player = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'sexe': self.sexe,
            'ranking': self.ranking,
        }
        return serialized_player

    def save(self):
        """ Save the player in the database. """
        serialized_player = self.serialize()
        self.manager.save_one(serialized_player)

    @classmethod
    def get(cls, serialized_player):
        """ Create an instance of player. """
        return cls.manager.get_one(serialized_player)

    @classmethod
    def get_all(cls):
        """ Get all player in the database and create instance of them. """
        return cls.manager.get_all()

    def __str__(self):
        return f"{self.last_name} {self.first_name}: rang({self.ranking})"

    def __repr__(self):
        return f"{self.last_name} {self.first_name}: rang({self.ranking})"


if __name__ == '__main__':
    yannick = Player('Yannick', 'Villain', '13-03-1977', 'M', 12)
    print(yannick.last_name)
    print(yannick.ranking)
    yannick.save()
