# Section 9: Python Functions, Loops & more Data Types
# While Loops (summation) file 2 
#! PART 1 
n = 0
while True:
    z = input('enter a number: ')
    
    if z.lower() == "done" or len(z) == 0:
        break
    
    n = n + int(z)
print(n)        

#! PART 2
x = 0

while True:
    y = input('enter a number: ')
    
    if y.lower() == "done" or len(y) == 0:
        break
    
    y = int(y)
    if y % 2 == 0:
        x = x + y
print(x)           

#! PART 3
x = 0

while True:
    y = input('enter a number: ')
    
    if y.lower() == "done" or len(y) == 0:
        break
    
    y = int(y)
    if y % 2 != 0 and y > 0:
        x = x + y
print(x)           

#! PART 4
x = 1

while True:
    y = input('enter a number: ')
    
    if y.lower() == "done" or len(y) == 0:
        break
    
    y = int(y)
    if y == 0: 
        continue
    else:
        x = x * y
print(x)

#! PART 5
list_number = []
x = 452 
while x <= 983:
    if x % 5 == 0 and x % 7 == 0:
        list_number.append(x)
    x+=1    

list_number.sort() 

max_number = list_number[-2]
min_number = list_number[1]
average = (max_number + min_number)/2
print(f'average number is: {average}')
           
