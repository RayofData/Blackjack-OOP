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
        return f"NPC: {self.name}, Cards: {cards_text}, Hand total: {self.get_hand_total()} Pot: ${self.total}"

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
        action = input(f"Hand total: {self.get_hand_total()}\nHit, Stand, or Double Down? ")

        if action.strip().lower().startswith(("d", "3")):
            self.double_down(deck)
            return

        while action.strip().lower().startswith(("h", "1")):
            self.hit(deck)
    
            if self.get_hand_total() >= 21:
                return
            action = input("Hit or Stand? ")
            
        self.stay()
     