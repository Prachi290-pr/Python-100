# Sort -  sort() ascending by default
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits)

# For descending order: reverse=True
numbers = [100, 50, 65, 82, 23]
numbers.sort(reverse=True)
print(numbers)


# sort() is case sensitive - Uppercase letters are sorted first
fruits2 = ["banana", "Orange", "Kiwi", "cherry","Watermelon", "kiwi"]
fruits2.sort()
print(fruits2)


# In order to avoid this, and make the sorting case-sensitive, we use str.lower
fruits2 = ["banana", "Orange", "Kiwi", "cherry","Watermelon", "kiwi"]
fruits2.sort(key=str.lower)
print(fruits2)


## Reverse List - reverse()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



## Copy List

# copy()
original = ['A', 'B', 'C']

list2 = original.copy()
print(list2)

# list()
list3 = list(original)
print(list3)

# slice
list4 = original[:]
print(list4)


## Join Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# Using +
list3 = list1 + list2
print(list3)

# Using append
for x in list2:
    list1.append(x)
print(list1)

# Using extend
list1.extend(list2)
print(list1)