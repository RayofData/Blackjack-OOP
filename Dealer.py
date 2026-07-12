from Player import Player

class Dealer(Player):
    def __init__(self, name, hands, seat=1):
        super().__init__(name, hands, seat)

    def print_hand(self):
        print(f"Dealer: {self.name}")
        current_hand = self.hands[0]
        print(f"Cards: {current_hand.get_hand_text()}\t{current_hand.get_hand_total_text()}")

    def action(self, deck):
        self.set_hand_total()
        while self.get_hand_total() < 17:
            self.hit(deck)