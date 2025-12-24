# ## Casting of datatypes
# # type() -  to get the datatype of a variable
#
# x = str(2)
# y = int(3)
# z = float(3)
#
# print(x)
# print(type(x))
#
# print(y)
# print(type(y))
#
# print(z)
# print(type(z))
#
# # case sensitive
# a = 2
# A = "Prachi"
#
# #---------
# ## Multiword variable names
#
# # Camel Case
# myNewVariable = 'John'
#
# # Pascal Case: All New word Upper case
# MyNewVariable = 2
#
# # Snake Case : _
# my_new_variable = 4
#
# #----------
# # x,y,z = 'A', 2, 'C'
# # print(x); print(y); print(z)
# #
# # x=y=z = "Same"
# # print(x)
# # print(y)
# # print(z)
#
# #---------
# # Unpacking a Collection
# fruits = ["apple", "banana", "cherry"]
#
# x,y,z = fruits
#
# print(x)
# print(y)
# print(z)
#
#
# #---------
# # Outputting variables
#
# x = "Python"
# y = "is"
# z = "awesome"
#
# a = 10
#
# print(x,y,z)
# print(x + y + z)   # not print(x+y+z) since there would be no space between the words then
#
# #print(x+a)    # we can only concatenate variables of same datatype
# print(x,a)     # this method works
#
# #-------------
#
# # Global Variables
# x = "awesome"
# def myfunc():
#     print("Python is", x)
#
# myfunc()
#
#
# y = 2
# def myage():
#     y = 21                         # global y : will keep the value of global variable (y=2) even inside the local function
#     print("I am",y,"years old")
#
# myage()
# print("My age is", y)
#
#
#
z = "awesome"


def newFunc():
    global z
    z = "nice"

newFunc()
print("Python is", z)