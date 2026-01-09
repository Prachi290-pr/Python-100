# Remove item - removes first occurrence of the specified item

fruits = ["apple", "banana", "cherry", "banana", "kiwi"]
fruits.remove('banana')
print(fruits)

# Remove Specified Index - pop(x)
fruits.pop(3)
print(fruits)

# pop() - removes last index item
fruits.pop()
print(fruits)

# Remove Specified Index - del
del fruits[1]
print(fruits)

# del - can be also used to delete the list completely
del fruits


# clear() - clears items in the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
