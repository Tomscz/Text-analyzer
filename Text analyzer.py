"""projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Šmíd
email: tomas.smid@gmail.com
discord: Tomáš Š#9081
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

line = (40 * "-")
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

# users input

username = input('Username:')
password = input('Password:')

if users.get(username) == password:

    print(f'Welcome to the app {username}, \nWe have 3 texts to be analyzed. ')
    print(line)

else:

    print('unregistered user, \nterminating the program..')
    quit()

# user choice

choice = input("Enter a number btw. 1 and 3 to select: ")

if choice.isnumeric() and 1 <= int(choice) <= 3:

    value = TEXTS[int(choice) - 1]

else:
    print("YOUR SELECTION IS NOT IN THE GIVEN RANGE")
    quit()

# empty lists

clean_words = list()
individual_words = (value.split())
title_words = list()
upper_words = list()
lower_words = list()
numbers_only = list()

# NUMBERS
# for loop

for word in individual_words:
    clean_words.append(word.strip(",.:;?!"))
    all_words_number = len(clean_words)

    if word.istitle():
        title_words.append(len(word))

    elif word.isalpha() and word.isupper():
        upper_words.append(len(word))

    elif word.islower():
        lower_words.append(len(word))

    elif word.isnumeric():
        numbers_only.append(int(word))

# output 1 - counts

print(f"There are {all_words_number} words in selected text.")
print(f"There are {len(title_words)} titlecase words.")
print(f"There are {len(upper_words)} uppercase words.")
print(f"There are {len(lower_words)} lowercase words.")
print(f"There are {len(numbers_only)} numeric string.")
print(f"The sum of all the numbers {sum(numbers_only)}")
print(line)
print(f"{'LEN':<3}|{'OCCURENCES':^13}|{'NUM':>5}")
print(line)

# STATISTIC
# lenght of all words in chosen tex

lenght_words = [(len(word)) for word in clean_words if word in clean_words]

# dict of individual lenght of words in chosen text key-lenght, value-occurence

number_lenght = {i: lenght_words.count(i) for i in set(lenght_words)}

for wordlenght, info in number_lenght.items():
    wordscount = info
    graph = wordscount * "*"

    # output 2 - statistic of occurence of words in chosen text + graph

    print(f"{wordlenght:<3}|{graph:<18} |{wordscount:>5}")
