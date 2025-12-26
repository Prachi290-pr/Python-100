print(10>5)
print(10==10)

# bool() -  Any string is true, all numbers are true (except 0). Sets, tuples, dict are False
print(bool("Hello"))
print(bool(15))
print(bool(0))
print(bool({}))   # [] () {}
print(bool(False))


# isinstance() - Checks if an object is of a certain datatype
x = 20
print(isinstance(x,int))