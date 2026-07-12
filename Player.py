from styling import colored_text, RED, GREEN, YELLOW, BLUE

class Player:
    def __init__(self, name, hands, seat):
        self.name = name
        self.hands = hands
        self.seat = seat

    def action(self, deck):
        pass

    def hit(self, deck, hand_index=0):
        print(colored_text("Hit!", YELLOW))

        card = deck.pop()
        card.state = "show"

        current_hand = self.hands[hand_index]
        current_hand.add_card(card)
        current_hand.get_hand_text()
        current_hand.get_hand_total_text()

        if current_hand.get_total() == 21:
            print(colored_text(f"{self.name} has 21!!", GREEN))
        elif current_hand.get_total() > 21:
            print(colored_text(f"{self.name} has BUSTED!!", RED))

    def stay(self):
        print("Stand.")

    def check_blackjack(self):
        current_hand = self.hands[0]
        if len(current_hand.cards) == 2 and current_hand.get_total() == 21:
            print(
                colored_text(
                    f"{self.name} has Blackjack!!",
                    GREEN
                )
            ) 
    def check_blackjack_boolean(self, hand_index=0):
        current_hand = self.hands[hand_index]
        return len(current_hand.cards) == 2 and current_hand.get_total() == 21 and self.total_hands() == 1

    def total_hands(self):
        return len(self.hands)
    
    def print_hand(self):
        pass


    
