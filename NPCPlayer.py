from Player import Player
import random

class NPCPlayer(Player):
    def __init__(self, name, seat, total, cards=[], hand_total=0, bet=0):
        super().__init__(name, cards, seat, hand_total)
        self.total = total
        self.bet = bet

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"NPC: {self.name}, Cards: {cards_text}, Hand total: {self.get_hand_total()} Pot: ${self.total}"

    def place_bet(self):
        self.bet = random.randint(1,3)*5
        self.total -= self.bet
    
    def double_down(self, deck):
        self.bet *= 2
        self.receive_card(deck.pop())

    def action(self, deck):
        if sum(self.cards.values) < 9:
            self.hit(deck)
        elif sum(self.cards.values) < 12:
            self.double_down(deck)
        elif sum(self.cards.values) < 16:
            self.hit(deck)
        else:
            self.stay() 