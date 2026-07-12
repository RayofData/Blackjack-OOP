from Player import Player
from styling import colored_text, RED, GREEN, YELLOW, BLUE

class Dealer(Player):
    def __init__(self, name, hands, seat=1):
        super().__init__(name, hands, seat)

    def print_hand(self):
        print(colored_text(f"Dealer: {self.name}", BLUE))
        current_hand = self.hands[0]
        print(colored_text(f"Cards: {current_hand.get_hand_text()}\t{current_hand.get_hand_total_text()}", YELLOW))

    def action(self, deck):
        hand = self.hands[0]
        total = hand.get_total()
        while total < 17:
            self.hit(deck)
            hand = self.hands[0]
            total = hand.get_total()