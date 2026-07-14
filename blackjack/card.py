from styling import colored_text, RED, GREEN, YELLOW, BLUE

class Card:
    def __init__(self, rank, suit, value, state):
        self.__rank = rank
        self.__suit = suit
        self.__value = value
        self.state = state

    def __str__(self):
        if self.state.lower() == "hidden".lower():
            return "Hidden"
        elif self.get_value() == 10 or self.get_value() == 11:
            return colored_text(f"{self.__rank} of {self.__suit}", GREEN)
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

    def ace_check(self):
        return self.__rank == "Ace" and self.state.lower() == "hidden"

    def ten_check(self):
        return self.__value == 10 and self.state.lower() == "hidden"

    
