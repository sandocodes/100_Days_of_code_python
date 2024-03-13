import pandas as pd


data = pd.read_csv('./nato_phonetic_alphabet.csv')

# Todo 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Todo 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

split_word = [letter for letter in word]

nato_code = [phonetic_dict[letter] for letter in split_word]
print(nato_code)

