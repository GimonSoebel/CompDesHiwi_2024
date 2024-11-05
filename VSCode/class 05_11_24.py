"""
heroes = ["Batman", "Wolverine", "Superman"]
 
for index, hero in enumerate(heroes):  
	print ("Index {} : {}".format(index,hero))
"""

# Outer loop for rows (1 through 10) 

for i in range(1, 11): 
	# Inner loop for columns (1 through 10) 

	for j in range(1, 11):
		# Print the product of the two numbers, end=" " keeps it on the same line 			
		print(i * j, end="\t") # \t adds a tab space between numbers
print() # Move to the next line after each row