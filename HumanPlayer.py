from Player import Player

class HumanPlayer(Player):
    def __init__(self, name, cards, seat, total, bet=0):
        super().__init__(name, cards, seat)
        self.total = total
        self.bet = bet

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"Player: {self.name}, Cards: {cards_text}, Pot: {self.total}"

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

    def stay(self):
        pass

    def action(self, deck):
        bet = input("Hit, Stand, or Double Down? ")
        if bet.lower().startswith("d"):
            self.double_down(deck)
            cards_text = ", ".join(str(card) for card in self.cards)
            print(cards_text)
        elif bet.lower().startswith("h"):
            self.hit(deck)
            cards_text = ", ".join(str(card) for card in self.cards)
            print(cards_text)
            if sum(card.value for card in self.cards) < 22:
                bet = input("Hit or Stand? ")
        else:
            self.stay()
    