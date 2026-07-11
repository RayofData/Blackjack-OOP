from Card import Card
from Table import Table
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



## Players
dealers = ["Sarah", "Robin", "Kat", "Austin", "Becky"]
random.shuffle(dealers)
npc_names = [
    "Alex",
    "Jordan",
    "Taylor",
    "Morgan",
    "Casey",
    "Riley",
    "Cameron",
    "Avery",
    "Dylan",
    "Jamie",
    "Logan",
    "Parker",
    "Quinn",
    "Reese",
    "Blake",
    "Hayden",
    "Sydney",
    "Emerson",
    "Rowan",
    "Charlie"
]
dealer = Dealer(dealers[0], []) # seat 1
table = Table([dealer])
table.print_table()

print("Welcome to Ray's Blackjack!")
print("This table has four available seats.")

num_players = int(input("How many human players are joining? "))
for i in range(num_players):
    name = input("Enter name: ")
    player = HumanPlayer(name,table.take_seat(name))


max_npcs = 5 - num_players
num_npcs = int(input(f"How many NPC players are joining? Maximum: {max_npcs} "))
pot = int(input("Enter the starting pot amount: $"))


    
npc1 = NPCPlayer("Steve", 3, 500)

# Stars new game with new shuffled deck
play_deck = deck
random.shuffle(play_deck)




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
            player.receive_card(play_deck.pop()) 
        else:
            card = play_deck.pop()
            card.state = "show"
            player.receive_card(card)



for player in table:
    print(player)
    if player.seat == 1:
        pass
    else:
        player.action(play_deck)