### Base code
import random

## Define Ddata Base fields using data structures

# Available materials
materials = {"concrete", "glas", "wood", "recycled plastic", "metal"}

# Available Element types
element_types = ["wall", "window", "door", "floor"]

# Available Rooms
rooms = ("living room", "bath", "kitchen", "bed room")

# Creating 10 random Elements
ElementDataBase = []

for i in range(10):
    element_id = f"P-00{i+1}"
    height = round(random.uniform(2.0, 5.0), 2)
    length = round(random.uniform(3.0, 10.0), 2)
    element_type = random.choice(element_types)
    material = random.choice(list(materials))
    room = random.choice(rooms)
    ElementDataBase.append((element_id, element_type, room, height, length, material))

print(ElementDataBase[1][0])

## Printing the database
print("\nE L E M E N T    D A T A B A S E:")

for element in ElementDataBase:
    print(
        "\n"
        "Element with ID: " + element[0] + " has a hight of " + str(element[3]) + " meters.",
        "\nAnd a length of " + str(element[4]) + " meters.",
        "\nIs made out of " + element[5] + ".",
        "\nBelongs to the " + element[1] + " Element-type.",
        "\nYou can find it in the " + element[2] + ".\n",
          )

print(
    "F O U R   Y O U R   I N F O:",
    "\nThe Database consists of " + str(len(ElementDataBase)) + " Elements.",
    "\nAnd " + str(len(ElementDataBase[0])) + " specific properties per Element.")

## Specific position of 1 Property out of 1 Element
specific_element = "kitchen"
position = None

# Search function (enumerate function from python forum)
for index, tupel in enumerate(ElementDataBase):
    if specific_element in tupel:
        position = (index, tupel.index(specific_element))
        break  # Brich die Schleife ab, sobald das Element gefunden wurde

if position:
    print(f"Element '{specific_element}' is at Position {position[0]} in List / Index {position[1]} in Tuple.\n")
else:
    print(f"Element '{specific_element}' was not found.\n")