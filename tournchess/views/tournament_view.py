class TournamentView:
    """ User interface using tournament model """

    def __init__(self, tournament_to_display=None):
        self.questions = []
        self.verification = False
        self.keys = []
        self.tournament_to_display = tournament_to_display

    def add_questions(self, question, question_variable, verify_question="", default_value=""):
        """ Add questions to the manager to create the tournament.
         Each question must contain the question, the variable name to save the question
         in a dictionary, the default_value and the test to verify the question"""
        self.questions.append((question, question_variable, verify_question, default_value))

    @staticmethod
    def ask_questions(question):
        """ Ask question to the manager. """
        return input(question)

    def display_responses(self):
        print(f"Vous venez de créer le tournoi suivant: \n"
              f"Nom du tournoi: {self.tournament_to_display.tournament_name}\n"
              f"Lieu du tournois: {self.tournament_to_display.tournament_place}\n"
              f"Dates: {self.tournament_to_display.date}")

    @staticmethod
    def display_information(informations):
        print(informations)

    def display_tournament_name(self):
        """ Display a list of all the tournaments."""
        if self.tournament_to_display:
            print("Voici la liste des tournois")
            for each_tournament in self.tournament_to_display:
                print(f"{each_tournament.tournament_name}, à {each_tournament.tournament_place},"
                      f" {each_tournament.date}")
        else:
            print("\nIl n'y a aucun tournoi dans la base de données")

    @staticmethod
    def display_laps(tournament):
        """ Display all the laps of a tournament. """
        for lap in tournament.laps:
            print(f"nom: {lap.lap_name}")
            print(f"Début: {lap.datetime_start} ; Fin: {lap.datetime_end}")

    @staticmethod
    def display_matches(tournament):
        """ Display all the matches in a tournament. """
        for lap in tournament.laps:
            print(f"nom: {lap.lap_name}")
            for match in lap.matches:
                print(f"{match.opponents}: vainqueur: {match.winner}")
