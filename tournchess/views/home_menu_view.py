class HomeMenuView:
    def __init__(self, menu_model):
        # menu est d du type HomeMenu
        self.menu_view = menu_model
        self.keys = []
        self.choice = True

    def display_menu(self):
        """ Display the menu """
        print("\nQue voulez-vous faire ?")
        for key, value in self.menu_view.menu_entries.items():
            print(f"{str(key)}- {value[0]}")

    def user_choice(self):
        for key in self.menu_view.menu_entries.keys():
            self.keys.append(key)
        self.display_menu()
        while self.choice not in self.keys:
            self.choice = input("\nQue voulez-vous faire ? Entrez le numero correspondant: ")
        return self.menu_view.menu_entries[self.choice][1]


class TournamentList:
    """ List all the tournaments in order to user choose one tournament """

    @staticmethod
    def choice_tournament(tournament_entries):
        """ The user can select a tournament. """
        for key, value in tournament_entries.items():
            print(f"{key}- {value.tournament_name}")
        return input("Entrez le numéro du tournoi choisi: ")

    @staticmethod
    def choice_tournament_in_progress(tournament_entries):
        """ The user can select a tournament in progress. """
        for key, value in tournament_entries.items():
            print(f"{key}- {value.tournament_name}")
        return input("Entrez le numéro du tournoi choisi: ")

    @staticmethod
    def display_informations(informations):
        print(informations)
