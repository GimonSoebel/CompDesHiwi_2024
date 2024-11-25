"""
Assignment 3: Building Information Modeling (BIM) Tool

Imagine you are developing a Building Information Modeling (BIM) Tool that stores information about different building elements.
Your task is to create a Python program that interacts with the user to collect and analyse data using dictionaries, built-in functions, UDFs or lambda. 
The program should perform the following tasks:

1.  Create a dictionary called building_elements that will store information about various building elements.
Each element should be identified by a unique key (e.g., a string or integer).
The value associated with each key should be another dictionary containing the following information: type, room, length, height, thickness.

key: The unique key for the element. (e.g. InW.01.23)
type: The type of the building element. (e.g., "wall," "window," "door," etc.).
room: The name of the room assigned to the building element. (e.g. "living room", "staircase" etc. )
length: The length of the element in meters.
height: The height of the element in meters.
thickness: The width of the element in meters.

2. Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
This function should contained the previous contained parameters:

3. Create a function called calculate_area that calculates and returns the area of a building element in m2.
Create a function called calculate_volume that calculates and returns the volume of a building element in m3.
The above two functions should take a key as a parameter and use the information from the building_elements dictionary to perform the calculations.

4. Create a function called get_elements_by_type that takes a type (e.g., "wall," "window," "door") as a parameter and
returns a list of keys for all building elements of that specific type.
"""

# 1. Initialize dictionary
building_elements = {
  'HE.0001': {
    'type': 'window',
    'room': 'foyer',
    'length': 0.5,
    'height': 1,
    'thickness': 0.01 
  }, 
  'HE.0002': {
    'type': 'door',
    'room': 'bedroom',
    'length': 1,
    'height': 2,
    'thickness': 0.04
  }, 
  'HE.0003': {
    'type': 'wall',
    'room': 'kitchen',
    'length': 15,
    'height': 3,
    'thickness': 0.15 
  }, 
}

# -------------------------------------------------------------------------------------------------------------------
# 2. Create add_element function

def add_element():
  # Maintain key naming format based on dictionary length
  if (len(building_elements) < 9):
    new_key = 'HE.000{}'.format(len(building_elements) + 1)
  elif (len(building_elements) >= 9 and len(building_elements) < 99):
    new_key = 'HE.00{}'.format(len(building_elements) + 1)
  elif (len(building_elements) >= 99 and len(building_elements) < 999):
    new_key = 'HE.0{}'.format(len(building_elements) + 1)
  else:
    new_key = 'HE.{}'.format(len(building_elements) + 1)

  # user input to define element type
  while True:
    new_type = (input('Please enter the type of element you would like to add: '))
    if (new_type.isalpha()):
      new_type = str(new_type)
      new_type = new_type.lower()
      break
    else:
      print ('Please input the type of element you wish to add as non-numerical text. Avoid special characters and spaces.')
  
  # user input to define room
  while True:
    new_room = (input('Please enter the name of the room this element is in: '))
    if (new_room.isalpha()):
      new_room = str(new_room)
      new_room = new_room.lower()
      break
    else:
      print ('Please input the name of the room as non-numerical text. Avoid special characters and spaces.')
  
  # user input to define length of the element
  length_bool = False
  while (length_bool == False):
    new_length = (input('Please enter the length of this element in meters: '))
    try:
      new_length = float(new_length)
      length_bool = True

    except ValueError:
      print ('Please input the length of this element as a number.')

  # user input to define the height of the element
  height_bool = False
  while (height_bool == False):
    new_height = (input('Please enter the height of this element in meters: '))
    try:
      new_height = float(new_height)
      height_bool = True

    except ValueError:
      print ('Please input the height of this element as a number.')

  # user input to define the thickness of the element
  thickness_bool = False
  while (thickness_bool == False):
    new_thickness = (input('Please enter the thickness of this element in meters: '))
    try:
      new_thickness = float(new_thickness)
      thickness_bool = True

    except ValueError:
      print ('Please input the thickness of this element as a number.')
  
  # add new element to the building elements dict
  new_dict = {new_key: {'type': new_type, 'room': new_room, 'length': new_length, 'height': new_height, 'thickness': new_thickness}}
  building_elements.update(new_dict)

  # ask user if they want to add more elements
  continue_bool = False
  while (continue_bool == False):
    add_more_elements = input('Would you like to add more elements? (y/n):')
    add_more_elements = add_more_elements.lower()

    print(add_more_elements)
    if (add_more_elements != 'y' and add_more_elements != 'n'):
      print("Please enter 'y' or 'n' to proceed.")
    elif (add_more_elements == 'y'):
      continue_bool = True
      add_element()
    else:
      continue_bool = True

# -------------------------------------------------------------------------------------------------------------------
# 3. Create calculation functions
# # Create a function that allows users to choose the element in the list they want to use for the calculations
def choose_element():
  choice_is_valid = False
  last_id_key = list(building_elements)[-1]

  while (choice_is_valid == False):
    choose_item = input('Please input the key of the desired element. (HE.0001 - {}):'.format(last_id_key))
    check_item = building_elements.get(choose_item)

    if (check_item == None):
      print('Please enter the key of an element in the database. Valid keys include HE.0001 - {}.'.format(last_id_key))
    else:
      choice_is_valid = True
      return choose_item

def calculate_area(element_to_eval): 
  eval_length = building_elements[element_to_eval]['length']
  eval_height = building_elements[element_to_eval]['height']

  element_area = (eval_length*eval_height)
  print('{} has an area of {} square meters.'.format(element_to_eval, element_area))
  return element_area

def calculate_volume(element_to_eval):
  area = calculate_area(element_to_eval)
  eval_thick = building_elements[element_to_eval]['thickness']

  element_volume = (area*eval_thick)
  print('{} has an volume of {} cubic meters.'.format(element_to_eval, element_volume))
  return element_volume

# -------------------------------------------------------------------------------------------------------------------
# 4. Create a function called get_elements_by_type
def get_elements_by_type():
  keys_list = []
  choose_type = input('What type of element would you like to look for in this database?: ')
  choose_type = choose_type.lower()

  # add matching items to keys_list
  for item in building_elements:
    if (building_elements[item]['type'] == choose_type):
      keys_list.append(item)
  
  # Print list of keys 
  if (len(keys_list) > 0):
    print ('The following keys are {}s in the database:'.format(choose_type))
    for key in keys_list:
      print(key)
  else:
    print('No elements of that type currently exist in this database.')

  return keys_list
  

      

# Run Functions
add_element()
analyze_element = choose_element()
calculate_volume(analyze_element)
get_elements_by_type()