from data import letters, numbers, symbols
import random


class Password:
    def __init__(self, num_letters, num_symbols, num_amount):
        self.how_many_letters = num_letters
        self.how_many_symbols = num_symbols
        self.how_many_numbers = num_amount

    def generate_letters(self):
        """ Generate Random Letters (a-zA-Z) """
        return random.choices(letters, k=self.how_many_letters)

    def generate_symbols(self):
        """ Generate Random Symbols """
        return random.choices(symbols, k=self.how_many_symbols)

    def generate_numbers(self):
        """ Generate Random Numbers (0 - 9) """
        return random.choices(numbers, k=self.how_many_numbers)
    
