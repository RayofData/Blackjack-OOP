from styling import colored_text, RED, GREEN, YELLOW, BLUE
from BettingPlayer import BettingPlayer

class HumanPlayer(BettingPlayer):
    def __init__(self, name, hands, seat, total, bet=0, insurance_bet=0 ):
        super().__init__(name, hands, seat, total, bet, insurance_bet)

    def print_hand(self):
        print(f"Player: {self.name}\tPot: ${self.total}")
        for i in range(self.total_hands()):
            current_hand = self.hands[i]
            print(f"Cards: {current_hand.get_hand_text()}\t{current_hand.get_hand_total_text()}")

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

        starting_hand = self.hands[0]
        card1 = starting_hand.cards[0].get_rank()
        card2 = starting_hand.cards[1].get_rank()
        pair = card1 == card2

        if pair:
            split = input(colored_text("Split? Y/N ", YELLOW))
            if split.strip().lower().startswith("y"):
                self.split(deck)

        starting_hand.get_hand_total_text()

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
            
            if starting_hand.get_hand_total() >= 21:
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