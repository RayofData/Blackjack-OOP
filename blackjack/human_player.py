from styling import colored_text, RED, GREEN, YELLOW, BLUE
from blackjack.betting_player import BettingPlayer

class HumanPlayer(BettingPlayer):
    def __init__(self, name, hands, seat, total, bet=0, insurance_bet=0 ):
        super().__init__(name, hands, seat, total, bet, insurance_bet)

    def print_seat_name(self):
         print(colored_text(f"Player: {self.name}", GREEN))

    def print_hand(self):
        current_hand = self.hands[0]
        print(f"Cards: {current_hand.get_hand_text()}\t{current_hand.get_hand_total_text()}")

    def ask_bet(self):
        while self.bet == 0:
            user_input = input(
                f"{self.name}, enter a bet or press Enter for Minimum bet $5: $"
            ).strip()

            if user_input == "" and self.total >= 5:
                bet = 5.0
            else:
                try:
                    bet = float(user_input)
                except ValueError:
                    print(colored_text("Bet must be a number.", RED))
                    continue

            if bet < 5:
                print(colored_text("Bet must be $5 or more.", RED))
            elif bet > self.total:
                print(colored_text(
                    f"Bet cannot exceed your balance of ${self.total:.2f}.",
                    RED
                ))
            else:
                self.place_bet(bet)

    # def check_split(self, deck):
    #     starting_hand = self.hands[0]
    #     card1 = starting_hand.cards[0].get_rank()
    #     card2 = starting_hand.cards[1].get_rank()
    #     pair = card1 == card2
    #     starting_hand.get_hand_text()
    #     if pair:
    #         split = input(colored_text("Split? Y/N ", YELLOW))
    #         if split.strip().lower().startswith("y"):
    #             self.split(deck)
                

    def action(self, deck, hand_index=0):
        self.hands[hand_index].get_hand_total_text()

        action = input(
            "1. Hit\n"
            "2. Stand\n"
            "3. Double Down\n"
            "Choose an action: "
        )

        if action.strip().lower().startswith(("d", "3")):
            if self.double_down(deck):
                return
            else:
                action = input(
                    "1. Hit\n"
                    "2. Stand\n"
                    "Choose an action: "
                )

        while action.strip().lower().startswith(("h", "1")):
            self.hit(deck)

            updated_hand = self.hands[0]
            if updated_hand.get_hand_total() >= 21:
                return

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
            print(f"{self.name} purchased No insurance.")