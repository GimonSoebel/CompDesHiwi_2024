width = input("What is the width of a room in meters? ")
length = input("What is the length of a room in meters? ")
height = input("What is the height of a room in meters? ")
#results as str

widthint = int(width)
lengthint = int(length)
heightint = int(height)
#results as int

volume = widthint*lengthint*heightint
area = widthint*lengthint
volumemilimeter = volume * 1000000000
areamilimeter = area * 1000000
#conversion to volume/area 

print("Your Room has a volume of " + str(volume) + "m³ and an area of " + str(area) + "m²")
print("Converted to milimeter you have a volume of " + str(volumemilimeter) + "mm³ and an area of " + str(areamilimeter) + "mm²") 
#Output of the  volumes/Areas

edgedim= [("width",widthint), ("length", lengthint), ("height", heightint)]
#converts the dimensions to tupples inside of a list

sorteddim = sorted(edgedim, key=lambda x: x[-1])
#sorts the list by the tuples second item
#used ChatGPT to explain the sorted function(lambda key)

#print(sorteddim)
smallest = sorteddim[0]
largest = sorteddim[-1]
#extracts the first/last item of the list 

print(f"The smallest dimension is {smallest[0]} with a value of {smallest[1]} meters.")
print(f"The largest dimension is {largest[0]} with a value of {largest[1]} meters.")




