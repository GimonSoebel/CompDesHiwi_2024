''' def for calculating area of the room, prints out the area in both formats'''
def calculateArea(width,length):
    print(f'Your room area in square meters is equal to: {width*length}, your room area in square mm is equal to: {width*length*1000**2}')

''' def for calculating volume of the room, prints out the volume in both formats'''    
def calculateVolume(width,length,height):
    print(f'Your room area in cubic meters is equal to: {width*length*height}, your room volume in cubic mm is equal to: {width*length*height*1000**3}')

''' def for finding the dominant of the values could be written smarter maybe with dictionaries'''
def find_dominant_dimension(width, length, height):
    if height > width and height > length:
        print( "The height of your room surpasses both its width and length.")
    elif width > length and width > height:
        print("The width of your room surpasses both its length and height.")
    elif length > width and length > height:
        print( "The length of your room surpasses both its width and height.")
    else:
        print( "Two or more dimensions are equal.")
'''cd
this part 'loops' through until user enter correct type value 
so basically make sure that float value is inputed if not its not True so it has to loop back to provide proper answer.
Also covers case when number is smaller or equal 0 -> in this case these are room's dimension so inputs need to be grater than 0.
'''
def get_valid_input(info):
    while True: 
        try:
            value = float(input(info))
            if value > 0:
                return value
            else:
                print("The value must be larger than 0 :c")
        except ValueError:
            print("It needs to be float/int value :c.")


user_width = get_valid_input('Please enter your room width in meters: ')
print('Thank you!!!')

user_length = get_valid_input('Please enter your room length in meters: ')
print('Dziekuje!!!')

user_height = get_valid_input('Please enter your room height in meters: ')
print('Danke schon!!')
print('............Performing calculations............')
calculateArea(user_width,user_length)
calculateVolume(user_width,user_length,user_height)
find_dominant_dimension(user_width,user_length,user_height)
print('it was tough... Necesito una cerveza ahora')



