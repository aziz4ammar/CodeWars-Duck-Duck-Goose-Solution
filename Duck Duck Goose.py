class Player:
    def __init__(self, name):
        self.name = name

def duck_duck_goose(players, k):
    index = (k - 1) % len(players)
    return players[index].name