from Player import Player
from styling import colored_text, RED, GREEN, YELLOW, BLUE
import random
import time

class Dealer(Player):
    def __init__(self, name, hands, seat=1):
        super().__init__(name, hands, seat)

    def print_seat_name(self):
         print(colored_text(f"Dealer: {self.name}", BLUE))

    def print_hand(self):
        current_hand = self.hands[0]
        print(colored_text(f"Cards: {current_hand.get_hand_text()}\t{current_hand.get_hand_total_text()}", BLUE))



    def action(self, deck):
        hand_total = self.hands[0].get_hand_total()
        time.sleep(1)

        while hand_total < 17:
            time.sleep(0.75)
            self.hit(deck)
            hand_total = self.hands[0].get_hand_total()

        if 17 <= hand_total < 22:
            time.sleep(0.75)
            self.stay()
            time.sleep(0.75)