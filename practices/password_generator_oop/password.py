from data import letters, numbers, symbols
import random


class Password:
    def __init__(self):
        self.letters = letters
        self.symbols = symbols
        self.numbers = numbers

    # Takes letters list
    def get_letters(self, n):
        """ Generate Random Letters (a-zA-Z). This method also takes 'n' as in the number of letters to generate """
        letters_list = random.choices(self.letters, k=n)

        letters = ""
        for letter in letters_list:
            letters += letter
        return letters

    def get_symbols(self, n):
        """ Generate Random Symbols. This method also takes 'n' as in the number of symbols to generate """
        symbols_list = random.choices(self.symbols, k=n)

        symbols = ""
        for symbol in symbols_list:
            symbols += symbol
        return symbols

    # Takes numbers list
    def get_numbers(self, n):
        """ Generate Random Numbers (0 - 9). This method also takes 'n' as in the amount of numbers to generate"""
        numbers_list = random.choices(self.numbers, k=n)

        numbers = ""
        for number in numbers_list:
            numbers += number
        return numbers

    def generate_password(self, letters_count, symbols_count, numbers_count):
        """ The method randomly shuffles the order of  the generated letters, symbols and numbers """
        random_letters = self.get_letters(letters_count)
        random_symbols = self.get_symbols(symbols_count)
        random_numbers = self.get_numbers(numbers_count)
        password_list = list(f"{random_letters}{random_symbols}{random_numbers}")

        # Shuffle password items in random order
        random.shuffle(password_list)

        # Turn password into string
        password = ""
        for item in password_list:
            password += item

        return password
