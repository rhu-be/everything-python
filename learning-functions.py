# A function = a block of reusable code
           # place () after the function name to invoke it

def bigthree(name, mc_name, age ):
    name = name.title()
    mc_name = mc_name.title()

    print(f"{name} is one of the big three.")
    print(F"The protagonist of {name} is {mc_name}.")
    print(F"He is {age} years old")


bigthree("one piece","Monkey . D . luffy", 19)
bigthree("Naruto", "Naruto uzumaki", 16)
bigthree("Bleach", "Ichigo kurosaki", 17)

#return = gives a value back to where the function was called.
def add (a, b):
    return a + b
result = add(1,7)
print(result)

def sub(a,b):
    return a - b
result = sub (1,7)
print (result)

def mult(a,b):
    return a * b
result =mult(1,7)
print(result)

def div(a,b):
    return a / b
result = div( 1, 7)
print(result)

# quick lesson on capitalize
# capitalize() = first letter of the first word is capitalized ie, Naruto uzumaki.
# title() = first letter of all words are capitalized ie, Naruto Uzumaki.
# upper() and lower() ensure all letters in a word are capitalized or small respectively ie, NARUTO UZUMAKI, naruto uzumaki




