import random

## Step 1
# suppliers
supplier = ["Home Depot", "Lowes", "BauHaus", "Ace Hardware", "A1 Building Supply", "A2 Building Supply"]

# room
room = ("bathroom ","kitchen", "main bedroom", "bonus room", "living room")

# Another field
type = {"floor", "ceiling", "door", "wall", "window"}


# length
length = [random.randint(1,6)]
    # print (length)

# length
height = [random.randint(1,6)]
    #  print (height)


## Step 2
ElementDataBase = [
    (random.choice(list(type)), room[random.randint(0,4)], supplier[random.randint(0,4)], random.randint(1,6), random.randint(1,6))
    ]

## extending the list
user_input_extend = input("Would you like to extend the database? Please input a number: ")
extend = int(user_input_extend)
for _ in range(extend):
    ElementDataBase.append((random.choice(list(type)), room[random.randint(0,4)], supplier[random.randint(0,4)], random.randint(1,6), random.randint(1,6)))


## Step3    
# print the entire database 
for item in ElementDataBase:
    print(f"type: {item[0]} - supplier: {item[2]} - location: {item[1]} - length: {item[3]}m - height: {item[4]}m")

# print the number of elements in the database
print(f"The database has {len(ElementDataBase)} elements")


# check that materials has at least 5 options
if len(supplier) >= 5:
    print(f"There are 5 or more unique suppliers used")
else:
    print("There are less than 5 unique suppliers used in this project")

# check the index and display
location_input = input(f"Would you like to seach the data base for a supplier? Please input a number <= than {len(ElementDataBase)}: ")
location = int(location_input)
print(f"the supplier of the item at index {location} is {ElementDataBase[location - 1][2]}")


# track the count of the user specifed material
user_input_material = input("Which supplier do you want to count? ")
count_material = sum(sub.count(user_input_material) for sub in ElementDataBase)
print(f"{user_input_material} is used {count_material} times")

    