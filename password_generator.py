import random

""" PASSWORD GENERATOR V1.0.0 """

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("******* PASSWORD GENERATOR *******\n\n")

while True:

    print(
        "Selezionare la complessità della password:\n1.BASSA (8 caratteri)\n2.MEDIA (12 caratteri)\n3.COMPLESSA (16 caratteri)\n4.Arbitrale(max 256)"
    )

    value = int(input().strip())  # Rimuove eventuali spazi o caratteri non visibili
    if value == 1:
        complexity = 8
        break
    elif value == 2:
        complexity = 12
        break
    elif value == 3:
        complexity = 16
        break
    elif value == 4:
        print("Inserire la lunghezza della password:")
        complexity = int(input())
        break
    else:
        print("Value not valid!\n")

temp = []
for i in range(complexity):
    temp.append(random.choice(letters + numbers + symbols))

random.shuffle(temp)
password = "".join(temp)

print("Password:\n" + password)