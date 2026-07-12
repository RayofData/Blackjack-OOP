from Player import Player
from styling import colored_text, RED, GREEN, YELLOW, BLUE

class BettingPlayer(Player):
    def __init__(self, name, seat, total, cards=None, hand_total=0, bet=0):
        if cards is None:
            cards = []

        super().__init__(name, cards, seat, hand_total)
        self.total = total
        self.bet = bet 

    def ask_bet(self):
        pass

    def place_bet(self, bet):
        self.bet = bet
        self.total -= self.bet 

    def split(self, deck):
        pass
        # split into two hands and double bet 

    def double_down(self, deck):
        if self.total >= self.bet:
            self.total -= self.bet
            self.bet *= 2
            print(colored_text(f"DOUBLE DOWN!! New bet ${self.bet}", YELLOW))
            self.hit(deck)
            return True
        else:
            print(colored_text("You do not have enough money to double down.", RED))
            return False

