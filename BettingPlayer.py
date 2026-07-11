from Player import Player

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
        self.bet *= 2
        self.hit(deck) 

