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
        hand_total = sum(card.value for card in self.cards)
        if hand_total > 21:
            cards_text = ", ".join(str(card) for card in self.cards)
            print(f"BUSTED total: {hand_total}")

    def stay(self):
        pass

    

    
