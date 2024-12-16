# loop list
from audloop import reverse

myList = ["eren", "selin", "luna", "ece"]

for x in myList:
    print(x)



# range(), len()
for i in range(len(myList)):
    print(myList[i])


# range(), len()
for i in range(0,4):
    print(myList[i])



# while loop
myList = ["eren", "ece", "selin", "luna"]
i = 0
while i < len(myList):
    print(myList[i])
    i = i + 1


###################
# list comprehension
myList = ["eren", "ece", "selin", "luna"]
[print(x) for x in myList]


# example
myList = ["eren", "ece", "selin", "luna"]
newlist = []

for x in myList:
    if "e" in x:
        newlist.append(x)

print(newlist)


# list comprehension example
myList = ["eren", "ece", "selin", "luna"]
newlist = [x for x in myList if "n" in x]
print(newlist)


# give me all except != "..."
newlist = [x for x in myList if x != "eren"]
print(newlist)


# iterable - range()
newlist = []
newlist = [x for x in range(9)]
print(newlist)


newlist = []
newlist = [x for x in range(1, 7)]
print(newlist)


# example
newlist = [x for x in range(10) if x < 5]
print(newlist)

# tüm listeyi büyük harfle yazar.
myList = ["eren", "ece", "selin", "luna"]
newlist = [x.upper() for x in myList]
print(newlist)

# elemanların baş harflerini büyük harfle yazar.
myList = ["eren", "ece", "selin", "luna"]
newlist = [x.capitalize() for x in myList]
print(newlist)


# Andrew NG (scientist)

# example
fruits = ["apple", "orange", "chery", "banana", "watermelon"]
newlist = [x if x != "chery" else "watermelon" for x in fruits]
print(newlist)

# sort list -alphabetically
fruits = ["apple", "orange", "chery", "banana", "watermelon"]
fruits.sort()
print(fruits)

# sort numbers,
numbers = [5, 6, 2, 1, 4, 3]
numbers.sort(reverse = True)
print(numbers)


# case insensitive sort
# sort method is case sensitive
thislist = ["apple", "Kiwi", "chery", "peanut", "Orange"]
thislist.sort()
print(thislist)


# perform a case-insensitive sort of the list
thislist = ["apple", "Kiwi", "chery", "peanut", "Orange"]
thislist.sort(key = str.lower)
print(thislist)


# copy a list
thislist = ["apple", "Kiwi", "chery", "peanut", "Orange"]
myList = thislist.copy()
print(myList)


# another way to make a copy is to use list() method
thislist = ["apple", "Kiwi", "chery", "peanut", "Orange"]
myList = list(thislist)
print(myList)


# example
thislist = ["apple", "Kiwi", "chery", "peanut", "Orange"]
myList = thislist[:3]
print(myList)


# python join list
thislist = ["apple", "Kiwi", "chery", "peanut", "Orange"]
numbers = [5, 6, 2, 1, 4, 3]
list3 = thislist + numbers
print(list3)


# append() method
thislist = ["apple", "Kiwi", "chery", "peanut", "Orange"]
numbers = [5, 6, 2, 1, 4, 3]

for x in numbers:
    thislist.append(x)

print(thislist)


# extend() method
thislist = ["apple", "Kiwi", "chery", "peanut", "Orange"]
numbers = [5, 6, 2, 1, 4, 3]

thislist.extend(numbers)
print(thislist)




# tuples
mytuple = ("apple", "Kiwi", "chery", "peanut", "Orange")

# unchangeable
# ordered
# tuples are written with round brackets
# tuple items are indexed, fist index 0, the second index
# allow duplicates


mytuple = ("apple", "apple", "kiwi", "chery", "peanut", "orange")
print(mytuple)

# tuple lenght
print(len(mytuple))



# create tuple with one item
thistuple = ("eren")
print(type(thistuple))



# tuple items can be any data type
# string, integer, float, boolean
tuple1 = ("eren", "selin") #string
tuple2 = (1, 2, 3, 10, 312, 8769) #integer
tuple3 = (1.1, 3.435, 5.4312414) #float
tuple4 = (True, False, True) #boolean


# a tuple can contain different data types
tuplemix = ("eren", 737, True, 7.37, "selin")
print(tuplemix)
type(tuplemix)


# tuple() constructor
mytuple = tuple(("eren", "selin"))
print(mytuple)


# access tuple items
mytuple = ("yusuf", "ömer", "buse", "mete", "mert", "rana", "eren")
print(mytuple[6])


# negative index
mytuple = ("yusuf", "ömer", "buse", "mete", "mert", "rana", "eren")
print(mytuple[-2:])



# range of index
mytuple = ("yusuf", "ömer", "buse", "mete", "mert", "rana", "eren")
print(mytuple[2:5])

mytuple = ("yusuf", "ömer", "buse", "mete", "mert", "rana", "eren")
print(mytuple[:3])

mytuple = ("yusuf", "ömer", "buse", "mete", "mert", "rana", "eren")
print(mytuple[3:])


# check if item exist
mytuple = ("yusuf", "ömer", "buse", "mete", "mert", "rana", "eren")
if "rana" in mytuple:
    print("yes, 'rana' is wearing a headscarf")


# change tuple items
x = ("yusuf", "ömer", "buse", "mete", "mert", "rana", "eren")
type(x) #tuple

y = list(x)
type(y)

print("hello")


