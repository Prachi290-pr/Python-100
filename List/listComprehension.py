# List comprehension - Shorter way to use/create lists             # 12:45

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


# shorter way

## newlist = [expression for item in iterable if condition == True]


newlist = [x.upper() for x in fruits if "a" in x]
print(newlist)

list2 = [x for x in fruits if "apple" in x]
print(list2)

list3 = [x for x in range(10)]
print(list3)

list4 = ["Hello" for x in range(10) if x < 5]
print(list4)