from Player import Player

class HumanPlayer(Player):
    def __init__(self, name, seat, total, cards=None, hand_total=0, bet=0):
        if cards is None:
            cards = []

        super().__init__(name, cards, seat, hand_total)
        self.total = total
        self.bet = bet

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"Player: {self.name}\tPot: ${self.total}\nCards: {cards_text}\tHand total: {self.get_hand_total()}"

    def place_bet(self):
        while self.bet == 0:
            bet = int(input(f"Minimal bet 5\n{self.name} Enter a bet: "))
            if bet < 5:
                print("Must be an amount of 5 or more.")
            elif bet > self.total:
                print(f"Bet must be less than total pot of ${self.total}")
            else:
                self.bet = bet
                self.total -= self.bet

    def split(self, deck):
        split = input("Split? Y/N ")
        if split.lower() == "y":
            pass
        # split into two hands and double bet
            
    
    def double_down(self, deck):
        self.bet *= 2
        self.hit(deck)

    def action(self, deck):

        if len(self.cards) == 2 and self.cards[0].get_rank() == self.cards[1].get_rank():
            self.split(deck)

        action = input(
            f"Hand total: {self.get_hand_total()}\n"
            "1. Hit\n2. Stand\n3. Double Down\nChoose an action: "
)

        if action.strip().lower().startswith(("d", "3")):
            self.double_down(deck)
            return

        while action.strip().lower().startswith(("h", "1")):
            self.hit(deck)
    
            if self.get_hand_total() >= 21:
                return
            action = input("Hit or Stand? ")
    