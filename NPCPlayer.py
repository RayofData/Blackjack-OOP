from Player import Player
import random

class NPCPlayer(Player):
    def __init__(self, name, seat, total, cards=None, hand_total=0, bet=0):
        if cards is None:
            cards = []

        super().__init__(name, cards, seat, hand_total)
        self.total = total
        self.bet = bet

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"NPC: {self.name}\tPot: ${self.total}\nCards: {cards_text}\tHand total: {self.get_hand_total()}"

    def place_bet(self):
        self.bet = random.randint(1,3)*5
        self.total -= self.bet
    
    def split(self, deck):
            if random.random() > 0.5:
                pass
            # split into two hands and double bet
            
    
    def double_down(self, deck):
        self.bet *= 2
        self.hit(deck)


    def action(self, deck):
        if self.get_hand_total() in range(9, 12):
            self.double_down(deck)
            return

        while self.get_hand_total() <= 15:
            self.hit(deck)
            
     