from styling import colored_text, RED, GREEN, YELLOW, BLUE

class Player:
    def __init__(self, name, cards, seat, hand_total=0):
        self.name = name
        self.cards = cards
        self.seat = seat
        self.__hand_total = hand_total

    def get_hand_total(self):
        return self.__hand_total

    def set_hand_total(self): 
        total = sum(card.get_value() for card in self.cards) 
        ace_count = sum(card.get_value() == 11 for card in self.cards)

        while total > 21 and ace_count > 0:
            ace_count -= 1
            total -= 10

        self.__hand_total = total
    
    def print_hand_total(self):
        print(colored_text(f"Hand total: {self.__hand_total}", YELLOW))

    def print_hand(self):
        print(", ".join(str(card) for card in self.cards))

    def receive_card(self, new_card):
        self.cards.append(new_card)   
        self.set_hand_total() 

    def action(self, deck):
        pass

    def hit(self, deck):
        print(colored_text("Hit!", YELLOW))
        card = deck.pop()
        card.state = "show"
        self.receive_card(card)
        self.print_hand()
        self.print_hand_total()

        if self.get_hand_total() == 21:
            print(colored_text(f"{self.name} has 21!!", GREEN))
        elif self.get_hand_total() > 21:
                print(colored_text(f"{self.name} has BUSTED!!", RED))

    def stay(self):
        print("Stand.")

    def check_blackjack(self):
        if len(self.cards) == 2 and self.get_hand_total() == 21:
            print(
                colored_text(
                    f"{self.name} has Blackjack!!",
                    GREEN
                )
            ) 
    def check_blackjack_boolean(self):
        return len(self.cards) == 2 and self.get_hand_total() == 21


    
