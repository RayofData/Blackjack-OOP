from Table import Table
from Room import Room
from Hand import Hand
from Dealer import Dealer
from HumanPlayer import HumanPlayer
from NPCPlayer import NPCPlayer
from styling import colored_text, RED, GREEN, YELLOW, BLUE
from helper import deck, dealers, npc_names
import random

##### Dealer #####
random.shuffle(dealers)
dealer = Dealer(dealers[0], [Hand()]) # seat 1

##### Create Table #####
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
room = Room(starting_balance)

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
    player = HumanPlayer(name, [Hand()], seat, starting_balance)
    table.take_seat(player)

# NPC players
max_npcs = table.table_size - table.current_table_size()
num_npcs = int(input(f"How many NPC players are joining? Maximum: {max_npcs} "))
random.shuffle(npc_names)

i = 0
while table.current_table_size() < table.table_size and i < num_npcs:
    seat = table.current_table_size() + 1
    name = npc_names[i]
    player = NPCPlayer(name, [Hand()], seat, starting_balance)
    table.take_seat(player)
    i += 1

## Start game loop
while table.current_table_size() > 1:
        
    # Everyone at table
    table.print_table()

    # Stars new game with new shuffled deck
    play_deck = deck.copy()

    for card in play_deck:
        card.state = "hidden"

    random.shuffle(play_deck)

    # Bets
    for person in table.persons[1:]:
        person.ask_bet()        

    # Deal cards
    for i in range(2):
        for j in range(table.current_table_size()):
            current_player = table.persons[j]
            current_hand = current_player.hands[0]
            card = play_deck.pop()

            if i == 0 and j == 0: 
                current_hand.add_card(card) 
            else:
                card.state = "show"
                current_hand.add_card(card)

    # Everyone at table
    table.print_table()
    dealer_seat = table.persons[0]
    dealer_hand = dealer_seat.hands[0]

    ##### Blackjack #####
    for current_player in table.persons[1:]:
        current_player.check_blackjack()

    ##### Check for Dealer Blackjack #####
    hidden_card = dealer_hand.cards[0]
    visible_card = dealer_hand.cards[1]

    # Insurance for dealer blackjack
    if visible_card.get_rank() == "Ace":
        print(colored_text("Dealer is showing an Ace.", RED))
        for current_player in table.persons[1:]:
            current_player.ask_insurance()

    
    # Check for dealer blackjack
    dealer_blackjack = (
        hidden_card.ace_check() and visible_card.get_value() == 10
    ) or (
        hidden_card.ten_check() and visible_card.get_value() == 11
    )

    if visible_card.get_rank() == "Ace" and not dealer_blackjack:
        print("Dealer did not have blackjack.")

    ##### Winners for dealer blackjack #####
    if dealer_blackjack:
        hidden_card.state = "show"
        dealer_hand.set_total()

        print(colored_text("Dealer has Blackjack!", RED))
        print(colored_text(str(dealer_seat), BLUE))

        for current_player in table.persons[1:]:
            for i in range(current_player.total_hands()):
                current_hand = current_player.hands[i]
                player_total = current_hand.get_hand_total()

                # Resolve insurance separately
                if current_player.insurance_bet > 0:
                    insurance_payout = current_player.insurance_bet * 3
                    current_player.total += insurance_payout

                    print(colored_text(
                        f"{current_player.name} wins the insurance bet. "
                        f"Payout: ${insurance_payout:.2f}.",
                        GREEN
                    ))
                    pass

            # Resolve the main hand
            if current_player.check_blackjack_boolean() and current_player.total_hands() == 1:
                current_player.total += current_player.bet

                print(colored_text(
                    f"{current_player.name} also has Blackjack. "
                    f"The main bet of ${current_player.bet} is returned.",
                    YELLOW
                ))
            else:
                print(colored_text(
                    f"{current_player.name} loses the main bet "
                    f"of ${current_player.bet} to dealer Blackjack.",
                    RED
                ))

    ##### Loop for rest of game play ######
    if not dealer_blackjack:         
        ##### Actions for hit, stay, double down and split #####
        for current_player in table.persons[1:]:
            for i in range(current_player.total_hands()):
                current_hand = current_player.hands[i]
                current_hand_total = current_hand.get_hand_total()
                table.persons[0].print_hand()
                current_player.print_hand()

                if current_hand_total != 21:
                    current_player.action(play_deck)

        ##### Dealer's Turn #####
        dealer_hand.cards[0].state = "show"
        dealer_hand.get_hand_text()
        dealer_seat.action(play_deck)
        updated_hand = dealer_seat.hands[0]
        updated_hand.set_total()
        dealer_total = updated_hand.get_total()


        ##### Winnings #####
        for current_player in table.persons[1:]:
            current_player.print_hand()
            for i in range(current_player.total_hands()):
                current_hand = current_player.hands[i]
                player_total = current_hand.get_hand_total()
                bet = current_player.bet + current_player.insurance_bet

                if current_player.check_blackjack_boolean():
                    payout = bet * 2.5
                    current_player.total += payout

                    print(colored_text(
                        f"{current_player.name} WINS with Blackjack! "
                        f"3:2 Payout: ${payout:.2f}.",
                        GREEN
                    ))

                elif player_total > 21:
                    print(colored_text(
                        f"{current_player.name} BUSTED with {player_total} "
                        f"and loses ${bet}.",
                        RED
                    ))

                elif dealer_total > 21:
                    payout = bet * 2
                    current_player.total += payout

                    print(colored_text(
                        f"{current_player.name} WINS with {player_total} "
                        f"because the dealer busted. Payout: ${payout}.",
                        GREEN
                    ))

                elif player_total < dealer_total:
                    print(colored_text(
                        f"{current_player.name} LOST with {player_total} "
                        f"against the dealer's {dealer_total} and loses ${bet}.",
                        RED
                    ))

                elif player_total == dealer_total:
                    current_player.total += bet

                    print(colored_text(
                        f"{current_player.name} PUSHED with {player_total} "
                        f"and receives the ${bet} bet back.",
                        YELLOW
                    ))

                else:
                    payout = bet * 2
                    current_player.total += payout

                    print(colored_text(
                        f"{current_player.name} WINS with {player_total} "
                        f"against the dealer's {dealer_total}. Payout: ${payout}.",
                        GREEN
                    ))

    ##### Table Reset ######
    for current_player in table.persons:
        current_player.hands = [Hand()]

    for current_player in table.persons[1:]:
        current_player.bet = 0
        current_player.insurance_bet = 0

    ##### Exit Table #####
    for current_player in table.persons[1:]:
        if current_player.total < 5:
            table.leave_table(current_player.seat, room)
            for seat, current_player in enumerate(table.persons, start=1):
                current_player.seat = seat

    if table.current_table_size() > 1:
        leave = input(
            "Would anyone like to leave the table? Enter Y or Yes to leave, "
            "or press Enter to continue: "
        )

    while leave.strip().lower().startswith("y"):
        table.print_table()

        try:
            seat = int(input("Enter the seat to leave: "))
        except ValueError:
            print(colored_text("Seat must be an integer.", RED))
            continue

        if seat == 1:
            print(colored_text("The dealer cannot leave the table.", RED))
        elif not 1 <= seat <= table.current_table_size():
            print(colored_text("That seat does not exist.", RED))
        else:
            table.leave_table(seat, room)

        for i, current_player in enumerate(table.persons, start=1):
            current_player.seat = i
        if table.current_table_size() > 1:
            leave = input(
                "Would another player like to leave the table? "
                "Enter Y or Yes to leave, or press Enter to continue: "
            )
        else:
            break

room.print_results()