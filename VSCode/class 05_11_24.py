"""
heroes = ["Batman", "Wolverine", "Superman"]
 
for index, hero in enumerate(heroes):  
	print ("Index {} : {}".format(index,hero))
"""

"""
# Outer loop for rows (1 through 10) 

for i in range(1, 11): 
	# Inner loop for columns (1 through 10) 

	for j in range(1, 11):
		# Print the product of the two numbers, end=" " keeps it on the same line 			
		print(i * j, end="\t") # \t adds a tab space between numbers
print() # Move to the next line after each row
"""

"""
user_input = ""
while user_input != "quit":
    user_input = input("Enter a command (type 'quit' to exit): ")
"""

"""
def calculate_dog_years():
    while True:
        age = input("Enter your age: ")
        if age.isdigit() and 0 < int(age) < 120:
            dog_years = 15 + 9 + (int(age)-2) * 5
            print ("You are {} years old in dog years".format(dog_years))
            break  # Exit the loop if age is a valid positive integer between 1 and 119
        else:
            print("Invalid input. Please enter a valid age.")

calculate_dog_years()
"""

