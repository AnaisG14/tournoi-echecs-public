class DisplayMatches:
    """ Display all the matches of a lap"""

    def __init__(self, tournament_in_progress):
        self.results = tournament_in_progress.results

    @staticmethod
    def display_players(players):
        """ Display the participants for a lap af a tournament. """
        print("Les joueurs suivants participent à ce tour :")
        for player in players:
            print(f"{player}; ")

    @staticmethod
    def display_score(matches):
        """ Display the scores at the end of a lap. """
        print("Voici les scores à la fin de ce tour")
        for match in matches:
            print(f"{match}")

    @staticmethod
    def display_matches(matches):
        """ Display the matches for the next lap. """
        print("Voici les matches pour ce tour")
        nb = 1
        for match in matches:
            print(f"Match {nb}: {match}")
            nb += 1

    def display_classement(self):
        """ Display the classement of a tournament. """
        print("\n Le tournoi est terminé.")
        self.results.sort(key=lambda x: x[1], reverse=True)
        print(f"Voici le classement pour ce tournoi:\n{self.results}")

    @staticmethod
    def ask_question(question):
        """ Ask questions to the manager. """
        response = input(question)
        return response

    @staticmethod
    def display_information(information):
        """ Display informations to the users. """
        print(information)
