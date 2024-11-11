from datetime import datetime
from .match import Match


class LapManager:
    """ serialize and deserialize players and save them into a tinyDB"""

    @classmethod
    def deserialize(cls, serialized_lap):
        """ To deserialize a serialize lap. """
        lap_name = serialized_lap['lap_name']
        matches = serialized_lap['matches']
        recreate_matches = []
        for serialized_match in matches:
            recreate_matches.append(Match.get(serialized_match))

        datetime_start = serialized_lap['datetime_start']
        datetime_end = serialized_lap['datetime_end']
        return {'lap_name': lap_name,
                'matches': recreate_matches,
                'datetime_start': datetime_start,
                'datetime_end': datetime_end
                }

    @classmethod
    def get(cls, deserialized_lap):
        """ get information of players using deserialize method"""
        lap = Lap(**deserialized_lap)
        return lap


class Lap:
    """ Model for a lap"""
    manager = LapManager()

    def __init__(self, lap_name, matches=None, datetime_start=None, datetime_end=""):
        self.lap_name = lap_name
        if matches:
            self.matches = matches
        else:
            self.matches = []
        self.serialized_matches = []
        if datetime_start:
            self.datetime_start = datetime_start
        else:
            self.datetime_start = datetime.now()
        self.datetime_end = datetime_end

    def add_match(self, new_match):
        """ Add a new match in the lap. """
        self.matches.append(new_match)

    def add_end_time(self):
        """ Add the end time of the lap. """
        self.datetime_end = datetime.now()

    def serialize(self):
        """ Serialize a match in order to save it. """
        for each_match in self.matches:
            serialized_match = each_match.serialize()
            self.serialized_matches.append(serialized_match)
        serialized_datetime_start = str(self.datetime_start)
        serialized_datetime_end = str(self.datetime_end)
        serialized_lap = {
            'lap_name': self.lap_name,
            'matches': self.serialized_matches,
            'datetime_start': serialized_datetime_start,
            'datetime_end': serialized_datetime_end,
        }
        return serialized_lap

    @classmethod
    def get(cls, serialized_lap):
        """ Recreate a match deserialized. """
        deserialized_lap = cls.manager.deserialize(serialized_lap)
        instance = cls(**deserialized_lap)
        return instance

    def __str__(self):
        return f"nom du tournoi: {self.lap_name}\n" \
               f"Matches: {self.matches}\n" \
               f"Heure début {self.datetime_start}"

    def __repr__(self):
        return f"nom du tournoi: {self.lap_name}\n" \
               f"Matches: {self.matches}"
