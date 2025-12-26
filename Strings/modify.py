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



## Format Strings

# Using f-strings
age = 32
text = f"My name is Prachi, im {age} years old"
print(text)

# Placeholder  :.
price = 58
text2 = f"The price is {price:.2f} dollars"
print(text2)

text3 = f"The price is {20*2} dollars"
print(text3)


## Escape characters
print("We are the so called \"Vikings\" of the north.")
print('We are the so called \'Vikings\' of the north.')