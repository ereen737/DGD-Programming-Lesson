#check python version
import sys
from faulthandler import cancel_dump_traceback_later

print(sys.version)

print("hello ai")

# for hashtag press alt + 3
# run selection
# first select the code and then shift + alt + e

# if you want to bring back your code press
# cmd + z


#numbers
3

5.5

3 + 2

4 * 5

if 9 > 3:
    print("nine is greater than tree")

type(3) # integer
type(100) # integer
type(5.5) # float
type(5,5) # type error, not working

print("kemal")
type("kemal")


# commends
## comments can be used to explain python code
## comments can be used to make the code more readable
## comments can be used to prevent when testing code
type(5.5) # float


# This is a comment
print("hello word!")


# comments can be placed at the end of a line and python ignores the rest of the line
print("hello world!") # this is a comment


# to add a multi-line comment, you can add a # to each line

# it's a comment
# you need to fix this code
# look at the data again
print("kemal")

# if you want tı add a multi-line string to your script, you can do so with """ triple quotes.

def multiplication(x, y):
    """
    this is a function comment
    :param x:
    :param y:
    :return:
    """
    print(x * y)

multiplication(1,2)


def add(x, y):
    """ this is addition function
        add two numbers for x and y
    """

    print(x + y)

add(5, 2)


# Python Variables
## Variables are used to store data values

# Creating variables
# A variable is created the first time you assign a value to variable

var1 = 5
var2 = 3
print(var1)
print(var2)


var1 * var2


# Variables can change type after they are set and are not required to be stated with a certain type.
# Example
x = 9 # is of type of int.
type(x)

x = "james" # x is now of the type str
type(x)


# Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(9)
type(x)

x = int(9) # y will be integer
type(x)

x = float(9) # x will be float
type(x)
print(type(x))


# Get type
# You can get the data type of a variable with the type() function

x = 9
y= "Jason"
print(type(x))
print(print(y))


# single or double quotes?
## you can use single or double quotes

x = "Kemal"
x = 'kemal'
# They are the same

# Case-sensitive
# Variable names are case-sensitive.

x = 9
X = "kemal"

myvar = "kemal"
my_var = "kemal"
_my_var = "kemal"
myVar = "kemal"
MYVAR = "kemal"
myvar2 = "kemal"

# give a short name or a more descriptive name (age, name, total etc.)
# A variable name must start with a letter or the underscore charecter
# A variable cannot start with a number

# not assign, or used
2myvar = "kemal"
my-var = "kemal"
my var = "kemal"


# one value to multiple variables

x = y = z = "cat"
print(x)
print(y)
print(z)


# unpack collection

fruits = ["apple", "banana", "orange"]
x, y, z, = fruits
print(x)
print(y)
print(z)

# print() function is often used to output variables
print(x)

print(x, y, z)

# You can also use the + operator to output multiple variables

x = "python "
y = "is "
z = "great "
print(x + y + z)


x = 5
y = 10
print(x + y)

x = 5
y = "john"
print(x + y) # we get error
print(x, y)


x = str(5)
y = " john"
print(x + y)

# Global variables
x = "awesome"

def myfunc():
    print("python is " + x)

myfunc()


# if you create a variable with the same name inside a function, this variable will be local, amd
# can be used inside the function. Global variable with the same name will remain as it was,
# Global and with the original value.

x = "awesome"

def myfunc():
    x = "fantastic"
    print("python is " + x)

myfunc()

x


def myfunc():
    global x
    x = ("fanstastic")

myfunc()

print("python is " + x)
