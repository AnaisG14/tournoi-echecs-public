from operator import attrgetter

class Player:
    """ Creation of player """
    def __init__(self, last_name, ranking):
        self.last_name = last_name
        self.ranking = ranking

    def __str__(self):
        return f"{self.last_name}: {self.ranking}"

    def __repr__(self):
        return f"{self.last_name}: {self.ranking}"

player1 = Player('anais', 12)
player2 = Player('fred', 15)
player3 = Player('Laure', 4)
player4 = Player('Jeremi', 7)

players = [player1, player2, player3, player4]
print(players)
players_score = [[x, 0] for x in players]
print(players_score)
list_tri_joueur = sorted(players_score, key= lambda x: x[1])
print(list_tri_joueur)
joueurs_tri = sorted(players, key=attrgetter("ranking"))
print(joueurs_tri)
list_players_sorted = sorted(players_score, key=lambda x: x[0].ranking)
print(list_players_sorted)
players_score[0][1] = 4
players_score[1][1] = 3
print(players_score)
list_players_sorted = sorted(players_score, key=lambda x: (x[1], x[0].ranking))
print(list_players_sorted)