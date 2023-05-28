# Section 9: Python Functions, Loops & more Data Types
# Lesson 15 - List Comprehension project
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
# add two list for storage data user price and name item:
add_cart = []
num_item = []
# use whill loop :
while True:
 # print menu item and input user for choose:    
    print(menu_item)
    input_user_choose = int(input("Enter the number of your choise: "))
 #  use if fore user enter choose 1    
    if input_user_choose == 1:
        print("avivable item:")
        prin_item = [f"{index+1}. {item}: ${price}" for index, [item, price] in enumerate(available_items)]
        print(*prin_item, sep="\n")
        print("------------------------")
        input_get = int(input('enter the number of the item you want to want to go get (0 to return to previous menu):'))    
        if input_get == 0:
            continue
        elif input_get in range(1, 7):
            add_cart.append(available_items[input_get-1][1])
            num_item.append(available_items[input_get-1][0])
            print(f'{available_items[input_get-1][0]} added to cart.')
    elif input_user_choose == 2:
         #  use if fore user enter choose 2    
        print(f"Cart:\n{'-'*15}")
        if len(add_cart) == 0:
            print('You have not purchassed any product puy product and try again!')
        for i in range(len(add_cart)):
            print(f'{num_item[i]}: ${add_cart[i]}')
        print('-'*15)
        print(f'Total price of cart: ${sum(add_cart)}')
    elif input_user_choose == 3:
         #  use if fore user enter choose 3    
        print(f'Total price of cart: ${sum(add_cart)}')
    elif input_user_choose == 4:
         #  use if fore user enter choose 4 and exit programe     
        print("Final cart:")
        end_programe = [f'{num_item[i]}: ${add_cart[i]}' for i in range(len(add_cart))]
        print(*end_programe, sep="\n")
        print('-'*15)
        print(f'Total price of cart: ${sum(add_cart)}')
        exit()