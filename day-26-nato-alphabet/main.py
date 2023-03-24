# List Comprehension

import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alp = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alp_dict = {row.letter: row.code for (index, row) in nato_alp.iterrows()}
# print(nato_alp_dict)
# print(type(nato_alp_dict))
# # print(nato_data_frame)

# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
phonetic_code = [nato_alp_dict[letter] for letter in user_input]
print(phonetic_code)
