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

dealer = Dealer(dealers[0], []) # seat 1
table = Table([dealer])


print("Welcome to Ray's Blackjack!")
print("This table has four available seats.")

print("The game ends when you leave the table or run out of money.")
print("Each player begins with the same starting balance.")

starting_balance = int(
    input("Enter the starting balance for each player: $")
)

num_players = int(input("How many human players are joining? "))
for i in range(num_players):
    name = input("Enter name: ")
    seat = table.table_size() + 1
    player = HumanPlayer(name, seat, starting_balance)
    table.take_seat(player)


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


table.print_table()


# Stars new game with new shuffled deck
play_deck = deck
random.shuffle(play_deck)

# bet
for person in table.persons[1:]:
    person.place_bet()

# deal cards
for i in range(table.table_size()):
    for j in range(2):
        if i == 0 and j == 0:
            player.receive_card(play_deck.pop()) 
        else:
            card = play_deck.pop()
            card.state = "show"
            player.receive_card(card)



for i in range(table.table_size()):
    print(table.persons[i])
    if i == 0:
        pass
    else:
        player.action(play_deck)