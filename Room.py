from styling import colored_text, RED, GREEN, YELLOW, BLUE

class Room:
    def __init__(self, starting_balance):
        self.persons = []
        self.starting_balance = starting_balance

    def join(self, person):
        self.persons.append(person)

    def print_results(self):
        print("\nFinal Results")

        for person in self.persons:
            difference = person.total - self.starting_balance

            if difference > 0:
                result = colored_text(f"won ${difference}", GREEN)
            elif difference < 0:
                result = colored_text(f"lost ${abs(difference)}", RED)
            else:
                result = colored_text("broke even", YELLOW)

            print(f"{person.name}: ${person.total} remaining, {result}")