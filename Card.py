class Card:
    def __init__(self, rank, suit, value, state):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.state = state

    def __str__(self):
        if self.state.lower() == "hidden".lower():
            return "Hidden"
        else:
            return f"{self.rank} of {self.suit}"


    
