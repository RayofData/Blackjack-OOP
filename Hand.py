from Card import Card

class Hand(Card):
    def __init__(self, cards, hand_total=0):
        self.cards = cards
        self.__hand_total = hand_total

    def add_card(self, card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []

    def set_total(self):
        self.__hand_total = sum(card.get_value() for card in self.cards)

    def get_total(self):
        return self.__hand_total