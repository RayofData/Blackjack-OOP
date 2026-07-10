class Player:
    def __init__(self, name, cards, seat):
        self.name = name
        self.cards = cards
        self.seat = seat

    def receive_card(self, new_card):
        self.cards.append(new_card)

    def hit(self, deck):
        card = deck.pop()
        card.state = "show"
        self.receive_card(card)

    def stay(self):
        pass

    

    
