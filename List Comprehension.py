#Section 9: Python Functions, Loops & more Data Types
#Lesson 15 - List Comprehension project file 1 :
#Make the following numbers positive.
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
convert_number = [-abs(num) for num in nums]
print(convert_number)


#Create a new list with the square of the numbers in the given list.
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
square_number = [num**2 for num in nums]
square_number.sort()
print(square_number)


#create a new list with the scores as percent and each score in the format of 88%
scores = [75, 87, 93, 98, 82, 67, 91, 88]
grades_st = [f'{grade}%' for grade in scores]
print(grades_st)


#Make a list with all the items in the following list in lowercase.
fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"]
lower_case = [fruit.lower() for fruit in fruits]
print(lower_case)


#Write code to find the sum of the even numbers in the list.
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
sum_even = [num for num in nums if num %2 == 0 ]
print(sum(sum_even))


#Make a new list with prices in the following form .$10.99
#prices = [10.99, 20.99, 30.99, 40.99, 50.99]
#price_add = [f'${price}' for price in prices]
#print(price_add)

##Section 9: Python Functions, Loops & more Data Types
##Lesson 15 - List Comprehension project file 2 :

#Write code to find the sum of numbers that are divisible by 3 and between 20
# and 140 then print the numbers separated by a comma.
su_list = [x for x in range(20, 141) if x % 3 == 0]
print(sum(su_list))
print(su_list)

#Make a List with 20 random numbers between 100 and 1000.
from random import randint
lis_number = [randint(100, 1000) for _ in range(21)]
print(lis_number)

#Make list with 100 random numbers between 100 and 10,000 that are divisible by 3 and 5.
from random import randint
list_new = []
for num in range(101):
    ran_num = randint(100, 10_000)
    if ran_num%2==0 and ran_num%5==0:
        list_new.append(ran_num)
print(list_new)        

#Modify this list of words to make All words are uppercase.

words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will', 'there',
'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into', 'could',
'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like', 'then',
'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find', 'also',
'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through', 'long',
'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because', 'good',
'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world', 'very', 'still',
'nation', 'hand', 'life', 'tell', 'write', 'become' 
]
lis_upper_case = [word.upper() for word in words ]
print(lis_upper_case)

#Edit words list to gain the following outputs.
words = [
["Hello", "from", "Codezilla"],
["Python", "Course", "is", "awesome"],
["I", "enjoy", "learning", "Python", "with", "Codezilla"]
]
convert_list_string = [" ".join(lis) for lis in words]
convert_list_string_upper = ["-".join(lis) for lis in words]

print(convert_list_string)
print(str(convert_list_string_upper).upper())

#Convert all the following numbers into positivenumbers.
nums = [44, 64, -12, 0, -5, 34, -55, 67, -88, -99]
convert_number = [abs(num) for num in nums] 
print(convert_number)

#Flat the following nested list.
nested_list = [["Hello", "from", "Codezilla"],
["Python", "Course", "is", "awesome"],
["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

add_list_word = [word for lis in nested_list for word in lis ]
print(add_list_word)

#Make a list of tuples with the first element as the
#word and the second element as the length of theword.
words = ["Hello", "from", "Codezilla", "Python", "Course"]
tupl_len_word = ((word, len(word)) for word in words )
print(tuple(tupl_len_word))

# A list of available items
lis_add_cart = []
lis_num_item = []
available_items = [
    # Format: [item name, price]
['pixel phone', 500],
['lenovo computer', 1000],
['iphone phone', 800],
['macbook computer', 1500],
['dell computer', 1000],
['samsung phone', 700]
]
menu_item = """What would you like to do?
1. view avivable items andd add to cart
2. view cart
3. total price of cart 
4. quit
"""
lis_add_cart = []
lis_num_item = []

while True:
    print(menu_item)
    input_user_choose = int(input("Enter the number of your choise: "))
    
    
    if input_user_choose == 1:
        print("avivable item:")
        for index, [item, price] in enumerate(available_items):
            print(f"{str(index+1).zfill(2)}. {item}: ${price}")
    print("------------------------")    
    input_get = int(input('enter the number of the item you want to want to go get (0 to return to previous menu):'))        
    if input_get ==0:
        continue
    else:
        lis_add_cart.append(available_items[input_get-1][1])
        lis_num_item.append(available_items[input_get-1][0])
        print(f'{available_items[input_get-1][0]} added to cart.')
        if input_user_choose == 2:
            print(f"Cart:\n{'-'*15}") 
            for i in range(len(lis_add_cart)):
                print(f'{lis_num_item[i]}: ${lis_add_cart[i]}')
                print(lis_add_cart, lis_num_item)
