from BettingPlayer import BettingPlayer
import random

class NPCPlayer(BettingPlayer):
    def __init__(self, name, seat, total, cards=None, hand_total=0, bet=0):
        if cards is None:
            cards = []
        super().__init__(name, seat, total, cards, hand_total, bet)

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"NPC: {self.name}\tPot: ${self.total}\nCards: {cards_text}\tHand total: {self.get_hand_total()}"

    def ask_bet(self):
        bet = random.randint(1,3)*5
        self.place_bet(bet)
    
            
    



    def action(self, deck):
        if self.get_hand_total() in range(9, 12):
            self.double_down(deck)
            return

        while self.get_hand_total() <= 15:
            self.hit(deck)
            
     