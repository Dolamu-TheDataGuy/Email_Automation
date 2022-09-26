# TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"


with open("./input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    cor_name = [] # empty list to house stripped names
    for name in names:
        name = name.strip("\n")
        cor_name.append(name)
    print(cor_name)


with open("./input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in cor_name:
        new_letter = letter_content.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as written_letter:
            written_letter.write(new_letter)
