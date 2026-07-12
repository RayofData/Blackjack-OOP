from Player import Player
from styling import colored_text, RED, GREEN, YELLOW, BLUE

class BettingPlayer(Player):
    def __init__(self, name, hands, seat, total,  bet=0, insurance_bet=0):
        self.total = total
        self.bet = bet
        self.insurance_bet = insurance_bet

        super().__init__(name, hands, seat)
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
            print(colored_text(f"DOUBLE DOWN!! New bet ${self.bet:.2f}", YELLOW))
            self.hit(deck)
            return True
        else:
            print(colored_text("You do not have enough money to double down.", RED))
            return False

    def set_insurance_bet(self):
        self.insurance_bet = self.bet*0.5
        self.total -= self.insurance_bet
        print(f"{self.name} purchases insurance.")
