#1 hardcoded database
#element [ID, type, room, length, height, thickness, material]
example_list = [
    ["001","wall","living room", 10.0, 20.0, 0.5,"concrete"],
    ["002","window","bathroom", 2.0, 1.5, 0.1,"glass"],
    ["003","door","staircase", 2.0, 1.5, 0.1,"wood"],
]
print(example_list)

example_tuple = ("001","wall","living room", 10.0, 20.0, 0.5,"concrete")
print(example_tuple)

example_set = {"001","wall","living room", 10.0, 20.0, 0.5,"concrete"}
print(example_set)




# Create your own database of elements:
list_elements = []
x = 0

while True:
    answer = input("Do you want to add another element? (Say yes or no): ").lower()
    if answer == "yes":
        element_ID = x
        element_type = (input("What building element do you want to add?: "))
        element_length = float((input("What length is your {}?: ".format(element_type)))) #doesn't check for right data type input
        element_height = float((input("What height is your {}?: ".format(element_type))))
        element_material = (input("What material is your {}?: ".format(element_type)))
        list_temp = [element_ID, element_type, element_length, element_height, element_material]
        list_elements.append(list_temp)
        print(list_elements)
        x = x+1
    elif answer=="no":
        print("This is your database of elements: ", list_elements)
        break
    else:
        print("Enter either yes/no")



#2 Database in one List with nested tuples (random)
import random
list_elements = []
element_type_catalogue = ['wall', 'window', 'door', 'floor', 'column', 'beam']
element_material_catalogue = ['wood', 'concrete', 'steel', 'brick', 'gasoline']
x = 0

amount = int(input("How many random elements do you want: "))
while x < amount:
    element_ID = x
    element_type = random.choice(element_type_catalogue)
    element_length = (round(random.uniform(0.1, 10), 2))
    element_height = (round(random.uniform(0.1, 10), 2))
    element_material = random.choice(element_material_catalogue)
    temp_tuple = (element_ID, element_type, element_length, element_height, element_material)
    list_elements.append(temp_tuple)
    x = x+1

print(list_elements)



#3 Print details
print("Amount of elements in total: ", len(list_elements))
print("Amount of properties of an element: ", len(list_elements[0]))

i = 1
element_type_list = [sublist[i] for sublist in list_elements]
print(element_type_list)

if len(set(element_type_list)) > 5:
    print("You have more than 5 different types of elements!")
else:
    print("You have less than 5 different types of elements!")

a = random.randint(0,len(list_elements)-1)
b = random.randint(2,len(list_elements[0])-1)
random_property = list_elements[a][b]
print("Hi! Random property:", random_property, " of element:", list_elements[a][1], "is located on list row:", a, "and column", b)
#Print one specific property of one specific element and communicate its location on the list