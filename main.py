from Card import Card
from Dealer import Dealer
from HumanPlayer import HumanPlayer
from NPCPlayer import NPCPlayer
import random


ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
deck = []

for suit in suits:
    for i in range(13):
        deck.append(Card(ranks[i], suit, values[i], "hidden"))

random.shuffle(deck)

## Players
dealer = Dealer("Sarah", []) # seat 1
player1 = HumanPlayer("Ray", [], 2, 500) # name, hand, seat, total
npc1 = NPCPlayer("Steve", [], 3, 500)

table = [dealer, player1, npc1]
total_players = len(table)-1

# bet
for player in table:
    if player.seat == 1:
        pass
    else:
        player.place_bet()

# deal cards
for player in table:
    for i in range(2):
        if i == 0 and player.seat == 1:
            player.receive_card(deck.pop()) 
        else:
            card = deck.pop()
            card.state = "show"
            player.receive_card(card)

for player in table:
    print(player)

for player in table:
    if player.seat == 1:
        pass
    else:
        player.action(deck)