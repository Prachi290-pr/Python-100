a = "Hello there!"


# Upper and Lower case - upper(), lower()
print(a.upper())
print(a.lower())


# Stripping Whitespace
b = "   Hi my name is Prachi.   "
print(b.strip())


# Replace String
print(b.replace("Pr","S"))


# Splitting
c = "The best, things, in life are free!"
print(c.split())
print(c.split(", "))
print(c.split("e"))



## Concatenation

d = a + c
print(d)

e = a + " " + c
print(e)