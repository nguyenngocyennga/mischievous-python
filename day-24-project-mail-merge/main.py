# Files, Directories and Paths

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()
    # print(starting_letter)

# with open("Input/Names/invited_names.txt") as invited_names_file:
#     invited_names = []
#     for _ in invited_names_file.readlines():
#         name = _.strip()
#         invited_names.append(name)
#     # print(invited_names)
#
# for name in invited_names:
#     with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as ready_letter_file:
#         new_content = starting_letter.replace(PLACEHOLDER, name)
#         ready_letter_file.write(new_content)

with open("Input/Names/invited_names.txt") as invited_names_file:
    for _ in invited_names_file.readlines():
        name = _.strip()
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as ready_letter_file:
            new_content = starting_letter.replace(PLACEHOLDER, name)
            ready_letter_file.write(new_content)
