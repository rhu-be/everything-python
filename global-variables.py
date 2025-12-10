#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#create a variable inside a function with the same name and name as the global variable
x = ("awesome")

def myfunc():
    x = "fantastic"
    print("python is " + x )

myfunc()

print ("python is " + x )

# the above are local variables

#To create a global variable the global keyword is used

def myfunc():
    global x
    x = "awesome"
    print ("I am " + x )
myfunc()

# alternatively having the print outside the function still run. to be updted

def myfunc():
    global x
    x = "awesome"

myfunc()

print("He is " + x )

#The global keyword can be used to change the gglobal variable inside a function

x = ("awesome")

def myfunc():
    global x
    x = "not awesome"

myfunc()

print("Bullying is " + x)

