## Section 9: Python Functions, Loops & more Data Types
## Nested Loops project : 
#nested_lis = [
#    ["Hello", "from", "Codezilla"],
#["Python", "Course", "is", "awesome"],
#["I", "enjoy", "learning", "Python", "with", "Codezilla"]
#]  
## Flat a nested list in 2 Ways:
#convert_lis = []
## method 1:
#for lis in nested_lis:
#    convert_lis += lis
#print(convert_lis)
#
#conver_lis = []
### method 2:
#for lis in nested_lis:
#    conver_lis.extend(lis)
#print(conver_lis)
#
#conver_lis = []
### method 3:
#for lis in nested_lis:
#    for word in lis:
#        conver_lis.append(word)
#print(conver_lis)

## Section 9: Python Functions, Loops & more Data Types
## Nested Loops project part 2 : 
#numbers = [511, 260, 261, 912, 362, 473, 893, 277, 351, 494
#, 584 ,488 ,716 ,859 ,950 ,598 ,484 ,341 ,885, 486
#] 
## Find the smallest multiple of 9 in the following list:
#new_list = []
#for num in numbers:
#    if num % 9 == 0:
#        new_list.append(num)
#min_number = min(new_list) 
#print(f'the smallest multiple of 9 is: {min_number}')            


## Section 9: Python Functions, Loops & more Data Types
## Nested Loops project part 4 : 

numbers = [
-500, -694, -762, -445, -348, -361, -758,
-594, -954, -861, -610, -549, -336, -400, -600, -836,
-671, -573, -555, -390, -450, -811, -849, -870, -815, -694,
-951, -588, -484, -609, -674, -411, -408, -498, -649,
-541, -441, -839, -567, -898
]   
# Find the largest even number in the following list without using max and sort:
number_help = numbers[0]
for num in numbers:
    if num %2 == 0 and num > number_help:
        number_help = num
print(f'largest even number in the list: {number_help}')        