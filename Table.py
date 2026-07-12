from styling import colored_text, RED, GREEN, YELLOW, BLUE
from Room import Room

class Table:
    def __init__(self, persons=None, table_size=6):
        self.persons = [] if persons is None else persons
        self.table_size = table_size

    def take_seat(self, person):
        if len(self.persons) < self.table_size:
            self.persons.append(person)
        else:
            print("Table is full.")

    def leave_table(self, seat, room):
        i = seat - 1
        person = self.persons[i]
        if person.total < 5:
            print(colored_text(f"{person.name} LOST and leaves the table with ${person.total}.", RED))
        else:
            print(colored_text(f"{person.name} leaves with ${person.total}.", YELLOW))
        self.persons.pop(i)
        room.join(person)


    def print_table(self):

        for i in range(self.current_table_size()):
            person = self.persons[i]
            if i == 0:
                print(colored_text(f"Seat {i+1}: Dealer {person.name}", YELLOW))
            else:
                print(f"Seat {i+1}: {person.name}\t Pot: ${person.total:.2f}")

    def print_table_hands(self):
        for i in range(self.current_table_size()):
            person = self.persons[i]
            hand = person.hands[0]
            if i == 0:
                print(colored_text(f"Dealer: {hand.get_hand_text()}", BLUE))
            else:
                print(f"{person.name}: {hand.get_hand_text()}")

    def current_table_size(self):
        return len(self.persons)
    
