from .player import Player


class MatchManager:
    """ serialize and deserialize players and save them into a tinyDB"""

    @classmethod
    def deserialize(cls, serialized_match):
        serialized_player1 = serialized_match['opponents'][0]
        serialized_player2 = serialized_match['opponents'][1]
        winner = serialized_match['winner']
        return {'opponents': [[Player.get(serialized_player1[0]), serialized_player1[1]],
                              [Player.get(serialized_player2[0]), serialized_player2[1]]],
                'winner': winner
                }


class Match:
    """ Create an instance of match. """
    manager = MatchManager()

    def __init__(self, player1, player2, winner=""):
        """ player1 = [player, score]"""
        self.opponents = (player1, player2)
        if winner:
            self.winner = winner
        else:
            self.winner = None

    def modify_score(self, score):
        """ Modify the score of the players. """
        self.opponents[0][1] += float(score)
        self.opponents[1][1] += 1 - float(score)
        if float(score) == 1:
            self.winner = f"{self.opponents[0][0].last_name} {self.opponents[0][0].first_name}"
        elif float(score) == 0.5:
            self.winner = "match nul"
        else:
            self.winner = f"{self.opponents[1][0].last_name} {self.opponents[1][0].first_name}"

    def __str__(self):
        if self.winner:
            return f"{self.opponents[0]} contre {self.opponents[1]} ; gagnant: {self.winner}"
        else:
            return f"{self.opponents[0]} contre {self.opponents[1]}"

    def __repr__(self):
        # return f"{self.player1} contre {self.player2}"
        if self.winner:
            return f"{self.opponents[0]} contre {self.opponents[1]} ; gagnant: {self.winner}"
        else:
            return f"{self.opponents[0]} contre {self.opponents[1]}"

    def serialize(self):
        """ Serialized the match in order to save it. """
        serialized_player1 = self.opponents[0][0].serialize()
        serialized_player2 = self.opponents[1][0].serialize()
        serialized_match = {
            'opponents': [[serialized_player1, self.opponents[0][1]], [serialized_player2, self.opponents[1][1]]],
            'winner': self.winner
                      }
        return serialized_match

    @classmethod
    def get(cls, serialized_match):
        """ Recreate an instance of match whith deserialized data. """
        deserialized_match = cls.manager.deserialize(serialized_match)
        player1 = deserialized_match['opponents'][0]
        player2 = deserialized_match['opponents'][1]
        winner = deserialized_match['winner']
        instance = cls(player1, player2, winner)
        return instance
