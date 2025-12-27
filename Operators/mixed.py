##  ----------- Chained Comparison Operators -----------
x = 5
print(1 < x <10)



## ----------- Logical Operators -----------
print(1 < x and x < 10)    # AND
print(x > 4 or x < 10)     # OR

print(not(x > 3 and x < 8))  # NOT



## ----------- Identity Operators -----------

# is      - Returns TRUE if both the variables are stored in the same memory space
# is not  - Returns TRUE if both the variables are "not" stored in the same memory space

x = ["apple", "banana"]
y = ["apple", "banana"]


print(x is y)     # Compares memory address; if both variables point to the same object
print("x is equal to y (value)",x == y)     # Checks if value is same or not

print("x is not equal to y (memory space)",x is not y)

# It can be checked using id()
print(id(x))
print(id(y))

# Same object can be created by assignment
list2 = x

# Thus, these will have the same memory address
print(id(x))
print(id(list2))



## ----------- Membership Operators -----------

fruits = ["apple", "banana", "cherry"]
print('banana' in fruits)

print('pear' not in fruits)


# Membership in Strings
text = "Hello World"

print("H" in text)
print("hello" in text)    # Case Sensitive
print("z" not in text)