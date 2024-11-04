print("Hello i'm a student manager made by Simon Göbel (3739585) and here to help you collecting and analyzing data about your students. ")
print("First i need you to enter all the necessesary information about the students. So please follow the steps below :) ")

# Create an empty list called student_data to store information about ITECH students. 
# Each item in the list should be a tuple containing the student's name, age, and origin country (e.g., ("Alice", 25, "New York")).

student_data = [] 


# Use a while loop to repeatedly ask the user for information about ITECH students. 
# Prompt the user to enter name, age, and city. Create a tuple for each student and append it to the student_data list.
# If the user press the "q" key the while loop should end.

while True:  # While loop to repeatedly ask the user for the Data.

    while True:  # Another while loop to check for invalid inputs.
        name = input("Enter the name of the student: ")
        if name.isalpha():  # Checks if the input is alphabetic.
            break
        else:
            print("Invalid input. Please enter a valid name. ")
            
    while True:
        age = input("Enter the age of the Student: ")
        if age.isdigit():  # Checks if the input is numeric.
            break
        else:
            print("Invalid input. Please enter a valid age (numeric). ")

    while True:
        country = input("Enter the origin country of the student: ")
        if country.isalpha():  # Checks if the input is alphabetic.
            break
        else:
            print("Invalid input. Please enter a valid country. ")

    student_data.append((name, int(age), country))  # Creates tuples inside the student_data list.

    user_input = input("Type 'q' to exit the loop, or a differnt key to add another student: ")  # Gives the user the option to break or to continue the loop.
    if user_input.lower() == 'q':
        break

print("This is the complete list of all of your students: {}. ".format(student_data))

# After collecting students data, use a for loop to calculate and print the average age of the students. 

age_average = []
for a in range(len(student_data)):  
    student_ages = (student_data[a])  # Checks for every tuple in the student_data list.
    age_average.append(student_ages[1])  # Checks for every item with index 1 (age) in the tuple.

age_average_calc = sum(age_average) / len(age_average)  # Calculation to get the overall average.

print("The average age of the students in this list is {}. ".format(int(age_average_calc)))

# Create a set called students_countries to store unique countries.

student_countries = set([])  # Set doesnt allow duplicated data -> all the unique countries.

# Use a for loop to iterate through the student_data list and add each student country to the students_countries set.

for b in range(len(student_data)):
    countries = student_data[b]  # Checks for every tuple in the student_data list.
    student_countries.add(countries[2])  # Checks for every item with index 2 (country) in the tuple.

# Create a new list called young_students that includes the names of visitors who are younger than the average age.
# Use a for loop and an if statement to populate this list.

young_students = []
for d in range(len(student_data)):  
    young_student_name = student_data[d]  # Checks for every tuple in the student_data list.
    if young_student_name[1] < age_average_calc:  # Checks for every item with index 1 (age) in the tuple and continues with those below the average age.
        young_students.append(young_student_name[0])  # When if is correct: appends the names (index 0) to the young_students list.

# Print out the list of young students and the set of unique countries.

print("{} are students younger or equal to the overall average. ".format(young_students))
print("{} are the different countries the students live in. ".format(student_countries))

# Calculate and print the total number of students and the percentage of students under average age.

total_students = len(age_average)  # Total number equal to every tuple in student_data list -> equal to the len of the afe_average list.
percentage_under_average = (len(young_students) / len(age_average)) * 100  # Calculation to get the percentage under the average age.

print("In total there are {0} students and {1} percent from them are under the average age.  ".format(total_students,int(percentage_under_average)))
print("That's all, thank you for your time :D ")

# Include a brief explanation of your code and any insights you gained from the assignment.

"""
You can find a brief explanation of my code in the commentaries next to the code.
I gained a lot of understandment about the difference between tuples, sets and lists and how to use them.
Also i learned a bit about data management and how to use for and while loops. 
In total i think this assignment helped me a lot to understand the basics of coding in python better :)
"""