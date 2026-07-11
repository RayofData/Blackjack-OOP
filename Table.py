class Table:
    def __init__(self, persons=[]):
        self.persons = persons

    def take_seat(self, person):
        self.persons.append(person)

    def leave_table(self, seat):
        self.persons.remove(seat)

    def print_table(self):
        for i in range(len(self.persons)):
            print(f"Seat {i+1}: {self.persons[i]}")

    def table_size(self):
        return len(self.persons)
    
