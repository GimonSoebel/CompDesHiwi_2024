#Assignment No 1. 
#Task 1
width = float(input("What is the width of your room in meters?")) #The user input is tunred into float in order to be able to take all kinds of values 
length = float(input("What is the length of your room in meters?"))
height = float(input("What is the height of your room in meters?"))

#Task 2
area_meters = width*length
volume_meters = width*length*height

area_milimeters = area_meters*1e6 #turning m2 into mm2
volume_miilimeters = volume_meters*1e9 # turning m3 into m3

print(f"The area in square meters is: {round(area_meters,2)}\n"
      f"The volume in cubic meters is: {round(volume_meters,2)}\n"
      f"The area in square milimeters: {round(area_milimeters,2)}\n"
      f"The volume in cubic milimeters is: {round(volume_miilimeters,2)}")

#Task 3
#I wanted to use the least amount of if statements possible
#This is why I decided to sort the input in: largest, middle and smallest one
#That way I can build the 3 if statements at the end of the code

# 1. Step is making a dictionary that passes the input values to keys with their actual names - this way the value is always identified with the dimension it is for
vals = {
    "width": width,
    "length": length,
    "height": height
}

# 2. Then we sort the dictionary by the values, which would mean the second element in the dictionary
sorted_items = sorted(vals.items(), key=lambda item: item[1])

# 3. the sorted values would be connected to their keys, so in this step we can extract the smallest, middle and largest values and their "names"
small_dimension_name, small_dimension_value = sorted_items[0]
mid_dimension_name, mid_dimension_value = sorted_items[1]
large_dimension_name, large_dimension_value = sorted_items[2]

# With the if statements, we can differentiate between different scenarios, where the printed sentece will describe how the input values compare
if large_dimension_value == mid_dimension_value == small_dimension_value:
    print(f"All the dimesions are the same")
elif large_dimension_value == mid_dimension_value:
    print(f"The {large_dimension_name} is equal to {mid_dimension_name} and bigger than {small_dimension_name}")
else:
    print(f"The {large_dimension_name} of your room surpasses both its {mid_dimension_name} and {small_dimension_name}")
