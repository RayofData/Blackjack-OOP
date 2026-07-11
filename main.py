from Card import Card
from Table import Table
from Dealer import Dealer
from HumanPlayer import HumanPlayer
from NPCPlayer import NPCPlayer
import random

# Creates Deck
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
deck = []

for suit in suits:
    for i in range(13):
        deck.append(Card(ranks[i], suit, values[i], "hidden"))


## Dealer
dealers = ["Sarah", "Robin", "Kat", "Austin", "Becky"]
random.shuffle(dealers)

dealer = Dealer(dealers[0]) # seat 1
table = Table([dealer])

# Welcome
print("Welcome to Ray's Blackjack!")
print("This table has four available seats.")

print("The game ends when you leave the table or run out of money.")
print("Each player begins with the same starting balance.")

# Starting Pot for everyone
starting_balance = int(
    input("Enter the starting balance for each player: $")
)

# Human players
num_players = int(input("How many human players are joining? "))
for i in range(num_players):
    name = input("Enter name: ")
    seat = table.table_size() + 1
    player = HumanPlayer(name, seat, starting_balance)
    table.take_seat(player)

# Npc players
max_npcs = 5 - num_players
num_npcs = int(input(f"How many NPC players are joining? Maximum: {max_npcs} "))
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
shuffled_npc = npc_names
random.shuffle(shuffled_npc)

for i in range(num_npcs):
    seat = table.table_size() + 1
    name = shuffled_npc[i]
    player = NPCPlayer(name, seat, starting_balance)
    table.take_seat(player)


## Start game loop

# Everyone at table
table.print_table()

# Stars new game with new shuffled deck
play_deck = deck
random.shuffle(play_deck)

# Bet
for person in table.persons[1:]:
    person.place_bet()

# Deal cards
for i in range(2):
    for j in range(table.table_size()):
        current_player = table.persons[j]
        card = play_deck.pop()

        if i == 0 and j == 0: 
            current_player.receive_card(card) 
        else:
            card.state = "show"
            current_player.receive_card(card)

# Actions for hit, stay, double down and split
for i in range(table.table_size()):
    current_player = table.persons[i]
    print(table.persons[0])
    if i == 0:
        pass
    else:
        print(current_player)
        current_player.action(play_deck)