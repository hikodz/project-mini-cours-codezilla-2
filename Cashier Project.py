### Section 10: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 1:
##-------------------------------------

while True:
    print_word = input('>')
    
    if print_word == 'done':
        print('Done!')
        break
    
    if print_word.startswith('#') or len(print_word) == 0:
        continue
    print(print_word) 
### Section 10: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 2:
##-------------------------------------
import random
# data user : 
number_bot = random.randint(1, 100)
print(f'this number won removed for user (secret) : {number_bot} ')
number_user = None
list_guesse = []

# use loop while : 
while number_bot != number_user:
    number_user = int(input('Guess the number: '))
# append number for list :    
    list_guesse.append(number_user)
    
    if number_bot != number_user and number_user < number_bot:
        print('Too low, try again')
    elif number_bot != number_user and number_user > number_bot:
        print('Too high, try again')

print(f'You guessed the number in: {len(list_guesse)} ')
           
# Section 10: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 3:
#-------------------------------------
# find the first multiple of 7 in a list of numbers
numbers = [953, 776, 532, 665, 973, 683, 484, 499, 741, 980]
num_lst = 0

while numbers[num_lst] % 7 != 0:
    num_lst += 1
print(f'The first multiple "7" is: {numbers[num_lst]}')
# Section 9: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 4:
#-------------------------------------
list_score = []
while True:
    score_student = input('Enter a score (or type \'done\' to exit): ')
    
    if score_student == 'exit':
        break
    
    list_score.append(float(score_student))
    
    average_score = sum(list_score)/len(list_score)
print(f'The average of the scores is :{average_score:.2f}')        
# Section 9: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 5:
#------------------------------step1------------------------------
list_ranking = []

while True:
    product_name = input('Enter product name: ')
    
    if product_name == 'done' or len(product_name) == 0:
        break
    
    product_quantity = int(input('Enter quantity: '))
    product_price = float(input('Enter price: '))
    
    print(f'{"-"*12}\nproduct: {product_name}\nquantity: {product_quantity}\nprice: {product_price} EGY')
# append total to list :    
    total_price = product_quantity * product_price
    list_ranking.append(total_price)
    
    print(f'{"-"*12}\nTotal item cost: {total_price} EGY')
#------------------------------step2------------------------------

# print intro cashier    
print('Thank you for shopping with codezilla. Have a nice day!')
# ranking list 
list_ranking.sort(reverse = True)
print('Price in descending order:')

# now ranking price and use method : 
edit_number = 1
len_ranking = len(list_ranking)

while len_ranking > 0:
    print(f'Price {edit_number}: {list_ranking[-len_ranking]}')
    len_ranking -= 1
    edit_number += 1 
# print cost total use method sum:
print('-'*12)
print(f'Total cost is: {sum(list_ranking)}')    
### Section 10: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 6:
## Section 9: Python Functions, Loops & more Data Types
#!lesson 4 - While Loops (Cashier Project) !part 1:
#-------------------------------------

while True:
    print_word = input('>')
    
    if print_word == 'done':
        print('Done!')
        break
    
    if print_word.startswith('#') or len(print_word) == 0:
        continue
    print(print_word) 
### Section 10: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 2:
##-------------------------------------
import random
# data user : 
number_bot = random.randint(1, 100)
print(f'this number won removed for user (secret) : {number_bot} ')
number_user = None
list_guesse = []

# use loop while : 
while number_bot != number_user:
    number_user = int(input('Guess the number: '))
# append number for list :    
    list_guesse.append(number_user)
    
    if number_bot != number_user and number_user < number_bot:
        print('Too low, try again')
    elif number_bot != number_user and number_user > number_bot:
        print('Too high, try again')

print(f'You guessed the number in: {len(list_guesse)} ')
           
# Section 10: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 3:
#-------------------------------------
# find the first multiple of 7 in a list of numbers
numbers = [953, 776, 532, 665, 973, 683, 484, 499, 741, 980]
num_lst = 0

while numbers[num_lst] % 7 != 0:
    num_lst += 1
print(f'The first multiple "7" is: {numbers[num_lst]}')
# Section 10: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 4:
#-------------------------------------
list_score = []
while True:
    score_student = input('Enter a score (or type \'done\' to exit): ')
    
    if score_student == 'exit':
        break
    
    list_score.append(float(score_student))
    
    average_score = sum(list_score)/len(list_score)
print(f'The average of the scores is :{average_score:.2f}')        
# Section 10: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 5:
#------------------------------step1------------------------------
list_ranking = []

while True:
    product_name = input('Enter product name: ')
    
    if product_name == 'done' or len(product_name) == 0:
        break
    
    product_quantity = int(input('Enter quantity: '))
    product_price = float(input('Enter price: '))
    
    print(f'{"-"*12}\nproduct: {product_name}\nquantity: {product_quantity}\nprice: {product_price} EGY')
# append total to list :    
    total_price = product_quantity * product_price
    list_ranking.append(total_price)
    
    print(f'{"-"*12}\nTotal item cost: {total_price} EGY')
#------------------------------step2------------------------------

# print intro cashier    
print('Thank you for shopping with codezilla. Have a nice day!')
# ranking list 
list_ranking.sort(reverse = True)
print('Price in descending order:')

# now ranking price and use method : 
edit_number = 1
len_ranking = len(list_ranking)

while len_ranking > 0:
    print(f'Price {edit_number}: {list_ranking[-len_ranking]}')
    len_ranking -= 1
    edit_number += 1 
# print cost total use method sum:
print('-'*12)
print(f'Total cost is: {sum(list_ranking)}')    
### Section 9: Python Functions, Loops & more Data Types
# !lesson 4 - While Loops (Cashier Project) !part 6:
balance_user = 2500
option_atm = '''Welcome to the ATM. please selecte an option: 
1. Check balance
2. Withdraw
3. Deposit
4. Exit
'''
while True:
    print(option_atm)
    choose_user = input('Enter option number: ')
    
    if int(choose_user) == 1:
        print(f'Your balance is: ${balance_user}')
    
    if int(choose_user) == 2:
        amount_with = int(input('Enter Withdraw amount: '))
        if amount_with <= balance_user:
            balance_user -= amount_with
            print(f'Withdrawal successful. Your new balance is: ${balance_user}')
        else:
            print('Insufficient balance.')
    if int(choose_user) == 3:
        amount_deposit = int(input('Enter deposit amount: '))
        balance_user += amount_deposit
        print(f'Deposit successful. Your new balance is: ${balance_user}') 
    if int(choose_user) == 4:
        break               

