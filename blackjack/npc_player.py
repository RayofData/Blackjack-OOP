from blackjack.betting_player import BettingPlayer
import random
import time

class NPCPlayer(BettingPlayer):
    def __init__(self, name, hands, seat, total, bet=0, insurance_bet=0 ):
        super().__init__(name, hands, seat, total, bet, insurance_bet)

    def print_seat_name(self):
         print(f"NPC: {self.name}")

    def print_hand(self):
        current_hand = self.hands[0]
        print(f"Cards: {current_hand.get_hand_text()}\t{current_hand.get_hand_total_text()}")

    def ask_bet(self):
        bet = random.randint(1,3)*5
        if bet > self.total >= 5:
            bet = self.total                   
        self.place_bet(bet)
    

    def action(self, deck):
        time.sleep(1)

        if self.hands[0].get_hand_total() in range(9, 12):
            time.sleep(0.5)
            self.double_down(deck)
            return

        while self.hands[0].get_hand_total() <= 15:
            time.sleep(0.75)
            self.hit(deck)

        if self.hands[0].get_hand_total() > 21:
            return

        time.sleep(0.75)
        self.stay()
        time.sleep(1)

    def ask_insurance(self):
        insurance = random.random()
        if insurance > 0.5:
            self.set_insurance_bet()
        else: 
            print(f"{self.name} purchased No insurance")
            
     