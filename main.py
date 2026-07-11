from Card import Card
from Table import Table
from Dealer import Dealer
from HumanPlayer import HumanPlayer
from NPCPlayer import NPCPlayer
from styling import colored_text, RED, GREEN, YELLOW, BLUE
import random

##### Create Deck #####
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
deck = []

for suit in suits:
    for i in range(13):
        deck.append(Card(ranks[i], suit, values[i], "hidden"))


##### Dealer #####
dealers = ["Sarah", "Robin", "Kat", "Austin", "Becky"]
random.shuffle(dealers)

dealer = Dealer(dealers[0]) # seat 1
table = Table([dealer])
available_seats = table.table_size - table.current_table_size()



##### Welcome Message ######
print(colored_text("Welcome to Ray's Blackjack!", YELLOW))
print(f"This table has {available_seats} available seats.")

print("The game ends when you leave the table or run out of money.")
print("Each player begins with the same starting balance.")

##### Starting Pot for everyone #####
starting_balance = int(
    input("Enter the starting balance for each player: $")
)

##### Players creation #####
# Human players


while True:
    try:
        num_players = int(input("How many human players are joining? "))
    except ValueError:
        print(colored_text("Number of players must be an integer.", RED))
        continue

    if num_players < 0:
        print(colored_text("Number of players cannot be negative.", RED))
    elif num_players > available_seats:
        print(colored_text(f"Only {available_seats} seats are available.", YELLOW))
    else:
        break

for i in range(num_players):
    name = input("Enter name: ")
    seat = table.current_table_size() + 1
    player = HumanPlayer(name, seat, starting_balance)
    table.take_seat(player)

# NPC players
max_npcs = table.table_size - table.current_table_size()
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
random.shuffle(npc_names)

i = 0
while table.current_table_size() < table.table_size and i < num_npcs:
    seat = table.table_size + 1
    name = npc_names[i]
    player = NPCPlayer(name, seat, starting_balance)
    table.take_seat(player)
    i += 1


## Start game loop
while table.current_table_size() > 1:
        
    # Everyone at table
    table.print_table()

    # Stars new game with new shuffled deck
    play_deck = deck.copy()
    random.shuffle(play_deck)

    # Bets
    for person in table.persons[1:]:
        person.ask_bet()        

    # Deal cards
    for i in range(2):
        for j in range(table.current_table_size()):
            current_player = table.persons[j]
            card = play_deck.pop()

            if i == 0 and j == 0: 
                current_player.receive_card(card) 
            else:
                card.state = "show"
                current_player.receive_card(card)

    ##### Blackjack #####
    for i in range(1, table.current_table_size()):
        current_player = table.persons[j]
        if current_player.get_hand_total == 21:
            print(colored_text(f"{current_player.name} has Blackjack!!", GREEN))  

    # Everyone at table
    table.print_table()
    dealer_seat = table.persons[0]

    ##### Check for Dealer Blackjack #####
    hidden_card = dealer_seat.cards[0]
    visible_card = dealer_seat.cards[1]

    # Insurance for dealer blackjack
    if visible_card.get_rank == "Ace":
        pass # insurance bet to be set up
    
    # Check for dealer blackjack
    if (hidden_card.ace_check() and visible_card.get_value() == 10) or (hidden_card.ten_check and visible_card.get_value() == 11):
        print("Dealer Blackjack! No one wins.")
        for i in range(1, table.current_table_size()):
            current_player = table.persons[i]
            if current_player.get_hand_total == 21:
                current_player.total += current_player.bet
            current_player.bet = 0   

    ##### Actions for hit, stay, double down and split #####
    for i in range(1, table.current_table_size()):
        current_player = table.persons[i]
        print(colored_text(dealer_seat, BLUE))
        print(current_player)
        current_player.action(play_deck)

    dealer.cards[0].state = "show"
    print(colored_text(dealer, BLUE))
    dealer_seat.action(play_deck)

### Winners ###
    for i in range(1, table.current_table_size()):
        current_player = table.persons[i]
        print(current_player)
        if current_player.get_hand_total() > 21:
            print(colored_text(f"{current_player.name} BUSTED with {current_player.get_hand_total()} and loses ${current_player.bet}.", RED))
        elif current_player.get_hand_total() < dealer_seat.get_hand_total() and dealer_seat.get_hand_total() <= 21:
            print(colored_text(f"{current_player.name} LOST {current_player.get_hand_total()} compared to {dealer_seat.get_hand_total()} and loses ${current_player.bet}.", RED))
        elif current_player.get_hand_total() == dealer_seat.get_hand_total():
            print(colored_text(f"{current_player.name} PUSHED {current_player.get_hand_total()} compared to {dealer_seat.get_hand_total()} and wins back ${current_player.bet}.", YELLOW))
            current_player.total += current_player.bet
        else:
            print(colored_text(f"{current_player.name} WINS {current_player.get_hand_total()} compared to {dealer_seat.get_hand_total()} and wins a total of ${current_player.bet*2}.", GREEN))
            current_player.total += current_player.bet*2

    for i in range(table.current_table_size()):
        current_player = table.persons[i]
        current_player.cards = []
        current_player.bet = 0
        current_player.set_hand_total()