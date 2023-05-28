#-----new project---- calculator----
# section 8, lesson 15 
#greeting the user
print("Welcome our deer user to our modest calculator😊")
print("~"*25)
#get the operation from user
operation = input("-Please, enter the operation (must sperate between elements by space) :  ").split()
print("~"*25)
# check spaces 
if len(operation) != 3:
    statment = "you should sperate between elements with space "
    result = None
else:
    #assignment the elements 
    num_1, operator, num_2 = operation
    num_1 = float(num_1)
    num_2 = float(num_2)
    statment = "sorry, you added an unvalid operator"
    result = None
    # determine the kind of operation
    if operator == "+":
        result = num_1 + num_2
        statment = "the result of addition is"
    elif operator == "-":
        result = num_1 - num_2
        statment = "the result of subtraction is"
    elif operator == "*":
        result = num_1 * num_2 
        statment = "the result of multiplication is"
    elif operator == "/":
        result = num_1 / num_2 
        statment = "the result of division is"
    elif    operator == "**":
        result = num_1 ** num_2 
        statment = " the result of power is"
# show the result 

if result == None:
    print(f"{statment}" )
else:
    print(f"{statment} {result:.2f}")

#-----new project---- calculator----
# section 8, lesson 15 
#greeting the user
print("Welcome our deer user to our modest calculator😊")
print("~"*25)
#get the operation from user
operation = input("-Please, enter the operation (must sperate between elements by space) :  ").split()
print("~"*25)
# check spaces 
if len(operation) != 3:
    statment = "you should sperate between elements with space "
    result = None
else:
    #assignment the elements 
    num_1, operator, num_2 = operation
    num_1 = float(num_1)
    num_2 = float(num_2)
    statment = "sorry, you added an unvalid operator"
    result = None
    # determine the kind of operation
    if operator == "+":
        result = num_1 + num_2
        statment = "the result of addition is"
    elif operator == "-":
        result = num_1 - num_2
        statment = "the result of subtraction is"
    elif operator == "*":
        result = num_1 * num_2 
        statment = "the result of multiplication is"
    elif operator == "/":
        result = num_1 / num_2 
        statment = "the result of division is"
    elif    operator == "**":
        result = num_1 ** num_2 
        statment = " the result of power is"
# show the result 

if result == None:
    print(f"{statment}" )
else:
    print(f"{statment} {result:.2f}")

#-----new project---- calculator----
# section 8, lesson 15 
#greeting the user
print("Welcome our deer user to our modest calculator😊")
print("~"*25)
#get the operation from user
operation = input("-Please, enter the operation (must sperate between elements by space) :  ").split()
print("~"*25)
# check spaces 
if len(operation) != 3:
    statment = "you should sperate between elements with space "
    result = None
else:
    #assignment the elements 
    num_1, operator, num_2 = operation
    num_1 = float(num_1)
    num_2 = float(num_2)
    statment = "sorry, you added an unvalid operator"
    result = None
    # determine the kind of operation
    if operator == "+":
        result = num_1 + num_2
        statment = "the result of addition is"
    elif operator == "-":
        result = num_1 - num_2
        statment = "the result of subtraction is"
    elif operator == "*":
        result = num_1 * num_2 
        statment = "the result of multiplication is"
    elif operator == "/":
        result = num_1 / num_2 
        statment = "the result of division is"
    elif    operator == "**":
        result = num_1 ** num_2 
        statment = " the result of power is"
# show the result 

if result == None:
    print(f"{statment}" )
else:
    print(f"{statment} {result:.2f}")