from BettingPlayer import BettingPlayer
import random

class NPCPlayer(BettingPlayer):
    def __init__(self, name, hands, seat, total, bet=0, insurance_bet=0 ):
        super().__init__(name, hands, seat, total, bet, insurance_bet)

    def __str__(self):
        print(f"NPC: {self.name}\tPot: ${self.total}")
        for i in range(self.total_hands()):
            current_hand = self.hands[i]
            print(f"Cards: {current_hand.get_hand()}\t{current_hand.get_total()}")

    def ask_bet(self):
        bet = random.randint(1,3)*5
        if bet > self.total >= 5:
            bet = self.total                   
        self.place_bet(bet)
    
    def action(self, deck):
        if self.get_hand_total() in range(9, 12):
            self.double_down(deck)
            return

        while self.get_hand_total() <= 15:
            self.hit(deck)
        self.stay()

    def ask_insurance(self):
        insurance = random.random()
        if insurance > 0.5:
            self.set_insurance_bet()
            
     