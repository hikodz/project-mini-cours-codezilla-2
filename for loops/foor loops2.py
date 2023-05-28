numbers = [1, 2, 3, 4, 5]
square_numbers = []
for number in numbers:
    square_number = number ** 2 
    square_numbers.append(square_number)
print(square_numbers) 
scores = [75, 87, 93, 98, 82, 67, 91, 88]
each_score_list = []
for score in scores:
    new_score = f'{score}%'
    each_score_list.append(new_score)
print(each_score_list)    
fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"]
lower_case = []
for fruit in fruits:
    lower_word = fruit.lower()
    lower_case.append(lower_word)
print(lower_case)    
names = ["mohamed gouda", "islam mahfouz", "ayman hamed", "hassan ali", "mostafa mohamed"]
title_case = []
for name in names:
    title_word = name.title()
    title_case.append(title_word)
print(title_case)
user_word = input('Enter word: ')
user_word= user_word.replace(' ', '')
list_letter = []

for letter in user_word:
    
    list_letter.append(letter.upper())
print(list_letter)    
prices = [10.99, 20.99, 30.99, 40.99, 50.99]
new_list_price = []
for price in prices:
    edit_price = f'${price}'
    new_list_price.append(edit_price)
print(new_list_price)    
# A list of prices
prices = [75, 153, 635, 144, 356, 712, 675, 234]
result = 0
number_list = 0
for price in prices:
    result += price
    number_list += 1
average = result / number_list
print(average)   
 

    






