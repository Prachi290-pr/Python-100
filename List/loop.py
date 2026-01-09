thislist = ["apple", "banana", "cherry"]

# For Loop
for x in thislist:
    print(x)


for i in range(len(thislist)):
    print(thislist[i])


# While Loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1


# List Comprehension using For Loop

[ print("printed through list comprehension: ",x) for x in thislist ]