from styling import colored_text, RED, GREEN, YELLOW, BLUE

class Table:
    def __init__(self, persons=None, table_size=6):
        self.persons = [] if persons is None else persons
        self.table_size = table_size

    def take_seat(self, person):
        if len(self.persons) < self.table_size:
            self.persons.append(person)
        else:
            print("Table is full.")

    def leave_table(self, seat):
        person = self.persons[seat - 1]
        if person.total < 5:
            print(colored_text(f"{person.name} LOST.", RED))
        else:
            print(colored_text(f"{person.name} leaves with ${person.total}.", YELLOW))
        self.persons.pop(seat - 1)

    def print_table(self):
        for i in range(len(self.persons)):
            print(f"Seat {i+1}: {self.persons[i]}")

    def current_table_size(self):
        return len(self.persons)
    
