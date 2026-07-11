class Player:
    def __init__(self, name, cards, seat, hand_total=0):
        self.name = name
        self.cards = cards
        self.seat = seat
        self.__hand_total = hand_total

    def get_name(self):
        return self.name

    def get_hand_total(self):
        return self.__hand_total

    def set_hand_total(self): 
        self.__hand_total = sum(card.get_value() for card in self.cards) 
    
    def print_hand_total(self):
        print(f"Hand total: {self.__hand_total}")

    def print_hand(self):
        print(", ".join(str(card) for card in self.cards))

    def receive_card(self, new_card):
        self.cards.append(new_card)   
        self.set_hand_total()  
 
    def hit(self, deck):
        card = deck.pop()
        card.state = "show"
        self.receive_card(card)
        self.print_hand()
        self.print_hand_total()

        if self.get_hand_total() == 21:
            print("21!!")
        elif self.get_hand_total() > 21:
            print(f"BUSTED!!")

    def stay(self):
        pass

    

    
