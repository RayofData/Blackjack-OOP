from styling import colored_text, RED, GREEN, YELLOW, BLUE
from BettingPlayer import BettingPlayer

class HumanPlayer(BettingPlayer):
    def __init__(self, name, seat, total, cards=None, hand_total=0, bet=0):
        if cards is None:
            cards = []
        super().__init__(name, seat, total, cards, hand_total, bet)

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"Player: {self.name}\tPot: ${self.total}\nCards: {cards_text}\tHand total: {self.get_hand_total()}"

    def ask_bet(self):
        while self.bet == 0:
            bet = int(input(f"Minimal bet 5\n{self.name} Enter a bet: "))
            if bet < 5:
                print(colored_text("Must be an amount of 5 or more.", RED))
            elif bet > self.total:
                print(colored_text(f"Bet must be less than total pot of ${self.total}", RED))
            else:
                self.place_bet(bet)


    def action(self, deck):

        if len(self.cards) == 2 and self.cards[0].get_rank() == self.cards[1].get_rank():
            split = input(colored_text("Split? Y/N ", YELLOW))
            if split.strip().lower().startswith("y"):
                self.split(deck)

        self.print_hand_total()
        action = input(
            "1. Hit\n2. Stand\n3. Double Down\nChoose an action: "
)

        if action.strip().lower().startswith(("d", "3")):
            self.double_down(deck)
            return

        while action.strip().lower().startswith(("h", "1")):
            self.hit(deck)
    
            if self.get_hand_total() >= 21:
                return
            action = input("1. Hit\n2. Stand\nChoose an action:  ")
        self.stay()
    