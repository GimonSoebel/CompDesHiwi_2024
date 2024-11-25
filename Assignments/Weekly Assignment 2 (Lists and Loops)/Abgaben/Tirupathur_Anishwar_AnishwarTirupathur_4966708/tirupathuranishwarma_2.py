"""
Assignment 2: Populating a list of Building Elements

Imagine you are developing a Building Element Database that stores different fields (properties) to describe a database of different building elements.
Your task is to create a Python program that is hardcoded to automatically fill this database and visualize it:

1. Create hardcoded written Data Structures such as List, Sets, and Tuples that allow you to define a set of options for defining different properties of the elements in the database.
    -Minimum one List, one Set, one Tuple
    -Minimum 4 Data Structures
    -Include Length as one of the fields
    Optional: fill some of the Data structures with code instead of hardcoding it, but this will require loops or list comprehension    

Example of possible properties:
Id: unique Id.
type: The type of the building element. (e.g., "wall," "window," "door," etc.).
room: The name of the room assigned to the building element. (e.g. "living room", "staircase" etc.)
length: The length of the element in meters.
height: The height of the element in meters.
material: type of material
etc.

2. Write a series of code lines that fill the database in one List with nested tuples by referring to Data Structures that you defined before.
    -Use List.append, use List.extend, use indexing (e.g. myList[i] = 3)
    -Minimum 10 elements
    Optional challenge (but fun): Use Random by checking the python reference. E.g. Random.randint, Random.choice to fill some of the properties of the elements.

3. Print the Database with some added strings in a way that is nice to read
    -Print the entire database
    -Print the amount of elements
    -Check that one of your Data structures contains at least 5 different options or properties and communicate it
    -Print one specific property of one specific element and communicate its location on the list
    Optional challenge: requires more python knowledge
        -Print the 3 longest elements
"""
### Base code
import random
from PIL import Image

## 1.Define Ddata Base fields using data structures

# Art in a Gallery
artwork_names = ('Guernica', 'Starry Night', 'The Garden of Earthly Delights', 'The School of Athens', 'American Gothic', 'Nighthawks', 'The Great Wave off Kanagawa', 'Saint Francis of Assisi', 'The Thinker', 'A Sunday Afternoon on the Island of La Grande Jatte', 'Untitled (Perfect Lovers)')

# Artist Names
artists = ('Pablo Picasso', 'Vincent Van Gogh', 'Hieronymous Bosch', 'Raphael', 'Grant Wood', 'Edward Hopper', 'Hokusai', 'Kehinde Wiley', 'Rodin', 'Georges Seurat', 'Felix Gonzalez-Torres')

# Year Created
year_created = [1937, 1889, 1510, 1511, 1930, 1942, 1831, 2005, 1904, 1886, 1987]

# Price of each Piece
monetary_value = []
for x in range(len(artwork_names)):
    value = random.randint(10000000, 34000000)
    if value not in monetary_value:
        monetary_value.append(value)

# Convert to a set
monetary_value = set(monetary_value)

# Painting Dimensions in cm
heights = [349.3, 73.7, 205.5, 500, 78, 84, 24.6, 182.9, 189, 207.6, 34.3]
lengths = [776.5, 92.1, 384.9, 770, 65.3, 152, 36.5, 152.4, 98, 308, 68.6]


# Image File Paths
guernica_path = 'mini_assignments\\2024\MA-2\\my_Environment\\artwork-img\\Guernica.jpg'
starry_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\Starry_Night.jpg'
garden_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\Garden_of_Earthly_Delights.jpg'
school_path = 'mini_assignments\\2024\MA-2\\my_Environment\\artwork-img\\School_of_athens.jpg'
american_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\American_Gothic.jpg'
nighthawks_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\Nighthawks.jpg'
wave_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\kanagawa.jpg'
saint_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\saint_francis.jpeg'
thinker_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\Thinker.jpg'
sunday_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\sunday_afternoon.jpg'
untitled_path = 'mini_assignments\\2024\\MA-2\\my_Environment\\artwork-img\\Untitled_Perfect_Lovers.jpg' 

artwork_paths = (guernica_path, starry_path, garden_path, school_path, american_path, nighthawks_path, wave_path, saint_path, thinker_path, sunday_path, untitled_path)
## 2. Data base filling using Nested tuples into a List
gallery_database = []
access_index = 0 

for price in monetary_value:
#   Determine if artwork is part of permanent collection or is loaned
    loan_status = random.randint(0,1)
    if (loan_status == 0):
       loan_status = 'Permanent Collection'
    else:
       loan_status = 'On Loan'
    
    artwork_info = (artwork_names[access_index], artists[access_index], year_created[access_index], price, loan_status, heights[access_index], lengths[access_index], artwork_paths[access_index])
    gallery_database.append(artwork_info)

    access_index += 1

## 3.Printing Data Base
# Print Database
for artwork in gallery_database:
    # Print Artwork Title (Year Created), by Artists Name, which is worth $X. Collection Status
    print("This piece is {}({}), by {}, which is worth ${}. It measures {} cm x {} cm. {}.".format(artwork[0], artwork[2], artwork[1], artwork[3], artwork[5], artwork[6], artwork[4]))

# Print Number of Elements in Database
print('There are {} pieces in the collection'.format(len(gallery_database)))

# Check that one of your Data structures contains at least 5 different options or properties and communicate it
if (len(monetary_value) >= 5):
    print('The set monetary_value has at least 5 options in it')

# Print one specific property of one specific element and communicate its location on the list
element_choice = random.randint(0, len(gallery_database) - 1)
property_choice = random.randint(0, len(gallery_database[element_choice]) - 1)

print("{} is property index {} of element index {} in the Gallery Database.".format(gallery_database[element_choice][property_choice], property_choice, element_choice))

# Print the three longest elements
length_of_elements = []

for element in gallery_database:
    element_info = (element[6], element[0])
    length_of_elements.append(element_info)

length_of_elements.sort()
length_of_elements.reverse()

print(length_of_elements)
longest_elements = length_of_elements[0:3]

print("The {} is the third longest work of art.".format(longest_elements[2][1]))
print("The {} is the second longest work of art.".format(longest_elements[1][1]))
print("The {} is the longest work of art.".format(longest_elements[0][1]))

# Display An Artwork
view_artwork = False
artwork_choice = 0

while (view_artwork == False):
    user_choice = str(input("Would you like to view one of the artworks? (Y/N): "))
    user_choice = user_choice.upper()

    if (user_choice == 'Y'):
        input_is_valid = False
        while (input_is_valid == False):
            try:
                artwork_choice = int(input('''
                Here are the artworks on display:
                1. {}
                2. {}
                3. {}
                4. {}
                5. {}
                6. {}
                7. {}
                8. {}
                9. {}
                10. {}
                11. {}
                Please input the number of the piece you would like to see (1 - 11).: 
                '''.format(gallery_database[0][0], gallery_database[1][0], gallery_database[2][0], gallery_database[3][0], gallery_database[4][0], gallery_database[5][0], gallery_database[6][0], gallery_database[7][0], gallery_database[8][0], gallery_database[9][0], gallery_database[10][0])
                ))

                if (artwork_choice <= 0 or artwork_choice > 11):
                    print('Please input a number between 1 and 11 inclusive.')
                else:
                    input_is_valid = True
            
            except  ValueError or artwork_choice <= 0 or artwork_choice > 11:
                print('Please input a number between 1 and 11 inclusive.')
        
        displayed_artwork = Image.open(gallery_database[artwork_choice - 1][7])

        print('Now displaying {}.'.format(gallery_database[artwork_choice - 1][0]))
        displayed_artwork.show()

        view_artwork = True
    
    elif (user_choice == 'N'):
        view_artwork = True
    else:
        print("Please input 'Y' or 'N' to proceed.")