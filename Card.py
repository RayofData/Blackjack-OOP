class Card:
    def __init__(self, rank, suit, value, state):
        self.__rank = rank
        self.__suit = suit
        self.__value = value
        self.state = state

    def __str__(self):
        if self.state.lower() == "hidden".lower():
            return "Hidden"
        else:
            return f"{self.__rank} of {self.__suit}"

    def get_value(self):
        if self.state.lower() == "show".lower():
            return self.__value
        else:
            return 0

    def get_rank(self):
        if self.state.lower() == "show".lower():
            return self.__rank
        else:
            return "Hidden"



    
