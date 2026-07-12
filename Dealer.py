from Player import Player

class Dealer(Player):
    def __init__(self, name, cards=None, seat=1):
        if cards is None:
            cards = []

        super().__init__(name, cards, seat)

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"Dealer: {self.name}, Cards: {cards_text}"

    def action(self, deck):
        self.set_hand_total()
        while self.get_hand_total() < 17:
            self.hit(deck)