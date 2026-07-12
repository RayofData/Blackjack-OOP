from styling import colored_text, RED, GREEN, YELLOW, BLUE

class Hand:
    def __init__(self, cards=None):
        self.cards = [] if cards is None else cards
        self.__hand_total = 0
        self.set_total()

    def add_card(self, card):
        self.cards.append(card)
        self.set_total() 

    def clear_hand(self):
        self.cards.clear()
        self.set_total()

    def set_total(self):
        total = sum(card.get_value() for card in self.cards) 
        ace_count = sum(card.get_value() == 11 for card in self.cards)

        while total > 21 and ace_count > 0:
            ace_count -= 1
            total -= 10

        self.__hand_total = total

    def get_total(self):
        return self.__hand_total

    def get_hand_total_text(self):
        return (colored_text(f"Hand total: {self.__hand_total}", YELLOW))

    def get_hand_text(self):
        return f", ".join(str(card) for card in self.cards)


