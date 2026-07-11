from Player import Player

class HumanPlayer(Player):
    def __init__(self, name, seat, total, cards = [], hand_total = 0, bet=0):
        super().__init__(name, cards, seat, hand_total)
        self.total = total
        self.bet = bet

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"Player: {self.name}, Cards: {cards_text}, Hand total: {self.get_hand_total()} Pot: ${self.total}"

    def place_bet(self):
        while self.bet == 0:
            bet = int(input("Minimal bet 5: "))
            if bet < 5:
                print("Must be an amount of 5 or more.")
            elif bet > self.total:
                print(f"Bet must be less than total pot of ${player.total}")
            else:
                self.bet = bet
                self.total -= self.bet

    def split(self, deck):
        if len(set(self.cards)) == 1:
            split = input("Split? Y/N ")
            if split.lower() == "y":
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
    