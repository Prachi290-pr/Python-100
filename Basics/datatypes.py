# Datatypes

# Text: str
x = 'Abc'

# Numeric : int, float, complex
a = 10
b = 20.3; d = 32e3   #32 x 10 ^ 3
c = 1j

# Sequence : list, tuple, range
a_list = ["apple", "banana", "cherry"]
a_tuple = ("apple", "banana", "cherry")
a_range = range(6)

# Mapping : dict
a_dict = {"name" : "John", "age" : 36}

# Set : set, frozenset
a_set = {"apple", "banana", "cherry"}
y = frozenset({"apple", "banana", "cherry"})

# Boolean : bool
z = True

# Binary : bytes, bytearray
a_bytes = b"Hello"
w = bytearray(5)

# None type : NoneType
x = None


# Getting the data type :
print(type(x))



# Casting
# cannot convert complex to any other number format

x = 1
y = 3.22

floated_x = float(x)


# Random Number
import random

print(random.randrange(1,10))