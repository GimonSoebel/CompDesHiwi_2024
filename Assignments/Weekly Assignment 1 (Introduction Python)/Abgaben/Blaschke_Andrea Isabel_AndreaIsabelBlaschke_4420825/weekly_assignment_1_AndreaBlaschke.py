#ASSIGNMENT 01

room_width = input("What is the width of the room? (in Meters)")
room_length = input("What is the length of the room? (in Meters)")
room_height = input("What is the hight of the room? (in Meters)")

#Convert the Stringdata into Integers to be able to calculate my values
room_width = int(room_width)
room_height = int(room_height)
room_length = int(room_length)
a = room_length * room_width
v = room_length * room_height * room_width

#Calculate the Volume and Area in the corresponding unit 
#I have to convert the Integers to string to display the number as only information 
print("The Area of the Room is "+ str(a) +"m² and the Volume of the Room is " + str(v) + "m³.")

#Convert the Data I use to calculate into Integers so that the Values can be Calculated with
a_mm = int(a)/int(1000000)
v_mm = int(v)/int(1000000000)

#To display the Values as a Number I have to convert into String Data
print("The Area of the Room in square millimeters is " +str(a_mm)+ "mm² and the Volume in cubic millimeters is " +str(v_mm)+ "mm³.")

#Determin the Dominant Value
if room_width > room_height > room_length:
    print("The width of the Room surpasses its heigth and length!")

elif room_height > room_length > room_width:
    print("The height of the Room surpasses its length and width!")

else:
    print("The length of the Room surpasses its width and height!")