# Lists are mutable, ordered and allows duplicate values          11.15 -

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)


# len()
print(len(fruits))

# List can have multiple datatypes
list1 = ["abc", 34, True, 40, "male"]

# Access Items
print(fruits[1])
print(fruits[-1])
print(fruits[1:3])  #  inclusive [ ) exclusive
print(fruits[:6])
print(fruits[2:])

# check if exists
if "apple" in fruits:
    print("Yes, it's present")

# Change Item value
fruits[1] = "dragonfruit"
print(fruits)

fruits[3:4] = ['blackberry', 'watermelon']  # only changed orange (3) and not (4)
print(fruits)


# Insert values
fruits.insert(2,'papaya')   # added a new value at 3rd position
print(fruits)


# Append values - Adds items at the end of list
fruits.append('tomato')
print(fruits)

# Extend list - Appends another list to one list
regular = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

regular.extend(tropical)
print(regular)

# extend can be used to append any object to the list ( dict, set, tuples )
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)