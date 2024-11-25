# 1. Define database fields by using data structures
import random
type={"wall","window","door","roof","slab "}
room=("living room","bedroom","bathroom","kitchen","dining room","staircase")
material=["concrete","wood","clay","brick","glass"]
length=[random.randint(1,100) for _ in range(10)]
height=[random.randint(1,20) for _ in range(10)]

## 2. Data base filling using nested tuples into a List
## make an empty list
ElementDataBase = []
## turn set into list, so random can be used
type_list=list(type)
## create id and use loop to fill the list
id=1
while id<20:
    element=(id,random.choice(type_list),random.choice(room),random.choice(material),random.choice(length),random.choice(height))
    ElementDataBase.append(element)
    id+=1

### 3. Print Database
### print the whole ElementDataBase
for item in ElementDataBase:
    print(item)
### print the amount of elements
print("The amount of elements is:",len(ElementDataBase))
### check one of my data structures
if len(type) >= 5:
    print("The property 'type' has at least 5 options")
else:
    print("The property 'type' has less than 5 options")
### print one specific property of one specific element and communicate its location on the list
num_1=10
num_2=2
specific_element=ElementDataBase[num_1]
print("The specific property",specific_element[num_2],"is in the 'room' list at index",room.index(specific_element[num_2]) )
### print the 3 longest elements
ElementDataBase=sorted(ElementDataBase,key=lambda i:i[4],reverse=True)
print(ElementDataBase[0],ElementDataBase[1],ElementDataBase[2])