from styling import colored_text, RED, GREEN, YELLOW, BLUE
from BettingPlayer import BettingPlayer

class HumanPlayer(BettingPlayer):
    def __init__(self, name, seat, total, cards=None, hand_total=0, bet=0, insurance_bet=0 ):
        if cards is None:
            cards = []
        super().__init__(name, seat, total, cards, hand_total, bet, insurance_bet)

    def __str__(self):
        cards_text = ", ".join(str(card) for card in self.cards)
        return f"Player: {self.name}\tPot: ${self.total}\nCards: {cards_text}\tHand total: {self.get_hand_total()}"

    def ask_bet(self):
        while self.bet == 0:
            try:
                bet = int(input(f"Minimal bet 5\n{self.name} Enter a bet: $"))
            except ValueError:
                print(colored_text("Bet must be an integer.", RED))
                continue

            if bet < 5:
                print(colored_text("Must be an amount of 5 or more.", RED))
            elif bet > self.total:
                print(colored_text(
                    f"Bet must be less than total pot of ${self.total}",
                    RED
                ))
            else:
                self.place_bet(bet)


    def action(self, deck):
        pair = len(self.cards) == 2 and self.cards[0].get_rank() == self.cards[1].get_rank()
        if pair:
            split = input(colored_text("Split? Y/N ", YELLOW))
            if split.strip().lower().startswith("y"):
                self.split(deck)

        self.print_hand_total()

        action = input(
            "1. Hit\n"
            "2. Stand\n"
            "3. Double Down\n"
            "Choose an action: "
        )

        if action.strip().lower().startswith(("d", "3")):
            if self.double_down(deck):
                pass
            else: 
                action = input(
                "1. Hit\n"
                "2. Stand\n"
                "Choose an action: "
            )

        while action.strip().lower().startswith(("h", "1")):
            self.hit(deck)

            if self.get_hand_total() >= 21:
                break

            action = input(
                "1. Hit\n"
                "2. Stand\n"
                "Choose an action: "
            )

        self.stay()

    def ask_insurance(self):
        prompt = (
            colored_text(f"{self.name} Insurance costs ${self.bet*0.5:.2f}. ", YELLOW)
            + "Enter Y or Yes to place the insurance bet, or press Enter to decline: "
        )
        insurance = input(prompt)
        
        if insurance.strip().lower().startswith("y"):
            self.set_insurance_bet()
        else:
            print("No insurance.")