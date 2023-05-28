## Section 9: Python Functions, Loops & more Data Types
# Lesson 5 - Introduction to For Loops file 1 project #!part 1 :   
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_num = 0
for number in numbers:
    total_num += number
print(total_num)

# Lesson 5 - Introduction to For Loops file 1 project #!part 2 :  
numbers = [1, 2, 3, 4, 5]
for square in numbers:
    print(square ** 2)

# Lesson 5 - Introduction to For Loops file 1 project #!part 3 :
string = "Codezilla Python Course"
# remove space :
replace_space = string.replace(' ', '')

for letter in replace_space:
    print(letter) 

## Lesson 5 - Introduction to For Loops file 1 project #!part 4 :

# A list of prices for different items in dollars
prices = [10.99, 9.99, 15.99, 7.99, 12.99]
total_price_dol = 0
for number in prices:
    total_price_dol += number
print(f'${total_price_dol}')

# Lesson 5 - Introduction to For Loops file 1 project #!part 5 :

numbers = [1, 2, 3, 4, 5]
x = 1
for num in numbers:
    x *= num
print(x)    