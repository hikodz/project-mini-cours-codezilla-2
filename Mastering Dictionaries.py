# Section 9: Python Functions, Loops & more Data Types
# Lesson 20 - Mastering Dictionaries file 1 project 1:

menu = {
"Margherita Pizza": 100,
 "Pepperoni Pizza": 120,
  "Meat Lovers Pizza": 150,
   "Chicken Pizza": 130
}

while True:
    add_key = input('Enter the name of the item o add to the menu(Press Enter To Exit): ').title()
    if len(add_key) != 0:
        add_value = int(input('Enter item price: '))
        menu[add_key] = add_value
    else:
        print('-'*17)
        print('The New Menu:')
        for pizza, price in menu.items():
            print(f'{pizza}: {price:.2f} EGP')
        exit()

# Section 9: Python Functions, Loops & more Data Types
# Lesson 20 - Mastering Dictionaries file 1 project 2:
menu = {
"Margherita Pizza": 100,
 "Pepperoni Pizza": 120,
  "Meat Lovers Pizza": 150,
   "Chicken Pizza": 130,
    "Beef Burger": 100,
     "Chicken Burger": 80
}

while True:
    delete_item = input('Enter name to be deleted(Press Enter To Exit): ').title()
    if len(delete_item) != 0:
        if delete_item in menu.keys() :
            check_delete = input(f'Are you sure you want to delete {delete_item.title()}? (y/n): ')
            if check_delete == 'y':
                del menu[delete_item]
                print(f'{delete_item} has been deleted')
            elif check_delete == 'n':
                continue
            else:
                print('please enter \'y\' or \'n\'')
        else:
            print('Item not found')
    else:
        print('-'*17)
        print('The New Menu:')
        for item, price in menu.items():
            print(f'{item}: {price:.2f} EGP')
        exit()


# Section 9: Python Functions, Loops & more Data Types
# Lesson 20 - Mastering Dictionaries file 1 project 3:
menu = {
"Margherita Pizza": 100,
 "Pepperoni Pizza": 120,
  "Meat Lovers Pizza": 150,
   "Chicken Pizza": 130,
    "Beef Burger": 100,
     "Chicken Burger": 80
}

while True:
    update_item = input('Enter item name to be update (Press Enter To Exit): ').title()
    if len(update_item) != 0:
        if update_item in menu.keys() :
            new_price = int(input('Enter the new price: '))
            menu.update({update_item: new_price})
            print(f'{update_item} has been update')
        else:
            print('Item not found')
            continue
    else:
        print('-'*17)
        print('The New Menu:')
        for item, price in menu.items():
            print(f'{item}: {price:.2f} EGP')
        exit()


# Section 9: Python Functions, Loops & more Data Types
# Lesson 20 - Mastering Dictionaries file 1 project 4:

menu = {
"Margherita Pizza": 100,
 "Pepperoni Pizza": 120,
  "Meat Lovers Pizza": 150,
   "Chicken Pizza": 130,
    "Beef Burger": 100,
     "Chicken Burger": 80
}
chooser_user = """
1. Add new items
2. Remove items
3. Update items 
4. Exit
"""

while True:
    print(chooser_user)
    enter_choise = int(input('Enter your choise: '))
    if enter_choise == 1:
        add_value = int(input('Enter item price: '))
        add_key = input('Enter the name of the item o add to the menu(Press Enter To Exit): ')
        if len(add_key) != 0:
            menu[add_key.title()] = add_value
            print(f'{add_key} add in menu')
            print('-'*17)
        else:
            print('-'*17)
            continue
    elif enter_choise == 2:
        delete_item = input('Enter name to be deleted(Press Enter To Exit): ').title()
        if len(delete_item) != 0:
            if delete_item in menu.keys() :
                check_delete = input(f'Are you sure you want to delete {delete_item.title()}? (y/n): ')
                if check_delete == 'y':
                    del menu[delete_item]
                    print(f'{delete_item} has been deleted')
                    print('-'*17)
                else:
                    continue
            else:
                print('Item not found')
                print('-'*17)
        else:
            continue
    elif enter_choise == 3:
        update_item = input('Enter item name to be update (Press Enter To Exit): ').title()
        if len(update_item) != 0:
            if update_item in menu.keys() :
                new_price = int(input('Enter the new price: '))
                menu.update({update_item: new_price})
                print(f'{update_item} has been update')
                print('-'*17)
            else:
                print('Item not found')
                print('-'*17)
                continue
        else:
            continue
    else:
        print('-'*17)
        print('The New Menu:')
        for item, price in menu.items():
            print(f'{item}: {price:.2f} EGP')
        exit()


students = {
    "Mohamed Hassan": {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97},
        "school": "Codezilla"
    },
    "Ahmed Kamal": {"grades": {
    "math": 100,
    "english": 95,
    "science": 93,
    "arabic": 100,
    "history": 94},
    "school": "Codezilla"
},
"Ali Adel": {"grades": {
    "math": 85,
    "english": 83,
    "science": 87,
    "arabic": 100,
    "history": 90},
    "school": "Al-Azhar"
},
"Hossam Yehia": {"grades": {
    "math": 100,
    "english": 94,
    "science": 98,
    "arabic": 100,
    "history": 100},
    "school": "Al-Azhar"
    }
}

# add list for save avreage grades and name student :
dict_ranking = {}

# use for loop by used in calculate average :
for name, info in students.items():
    grade_student = [grade for subject, grade in info["grades"].items()]
    average_grades = sum(grade_student) / len(grade_student)
    dict_ranking = dict_ranking | {average_grades: name}

# use function max for know max grades in dict_ranking : 
max_grades = max(dict_ranking)
print(f'{dict_ranking[max_grades]} has the highest total percentage which is {max_grades:.2f}%\n{"-"*25}')

# use for loop by print subject and grade :
for subjec, grade in students[dict_ranking[max_grades]]["grades"].items():
    print(subjec, grade, sep=': ')


# Section 9: Python Functions, Loops & more Data Types
# Lesson 20 - Mastering Dictionaries file 1 project 4:
schools = {
"Codezilla":{
        "Mohamed Hassan":{
        "math": 100,
        "english": 90,
        "science": 85,
        "arabic": 100,
        "history": 97
        },
        "Ahmed Kamal":{
        "math": 100,
        "english": 95,
        "science": 93,
        "arabic": 100,
        "history": 94
        }
},
"Al-Azhar":{
        "Ali Adel": {
        "math": 85,
        "english": 83,
        "science": 87,
        "arabic": 100,
        "history": 90
        },
        "Mariam Ali": {
        "math": 100,
        "english": 94,
        "science": 98,
        "arabic": 100,
        "history": 100
        }
}}
average_grade_school = []
for school, info in schools.items():
    for student, grade in info.items():
        list_grade_student = [grade_subject for subject, grade_subject in grade.items()]
        average_grade_student = sum(list_grade_student) / len(list_grade_student)
        average_grade_school.append(average_grade_student)   
    total_average_school = sum(average_grade_school) / len(average_grade_school)
    print(f'The Average Total for {school} school is: {total_average_school:.2f}')
    average_grade_school.clear()
    print('-'*30)

inventory = {

"Paracetamol": {"price":25, "quantity":10},
"Aspirin": {"price":15, "quantity":20},
"Ibuprofen": {"price":20, "quantity":15},
 "Cough Syrup": {"price":30, "quantity":5},
  "Augmentin": {"price":100, "quantity":7},
   "Amoxicillin": {"price":80, "quantity":8},
    "Panadol": {"price":25, "quantity":10},
     "Zinc": {"price":15, "quantity":20}, 
     "Vitamin C": {"price":20, "quantity":15},
      "Fucidin": {"price":30, "quantity":5},
       "Kolanog": {"price":100, "quantity":2},
}
info_programe = '''
1. add new item
2. remove item
3. update item
4. check avivable quantity
5. print treatement information
6. show all item with price and quantity
7. exit
'''

vanilia_prog ='---Entering new item---'
while True:
    print(info_programe)
    input_choose = int(input('Enter your choice: '))
    if input_choose == 1:
        print(vanilia_prog)
        name_item_new = input('Enter item new (press enter to exit): ').title()
        if len(name_item_new) != 0:
            price_item = int(input('Enter item price: '))
            quantity_item = int(input('Enter item quantity: '))
            inventory = inventory | {name_item_new:{'price': price_item, 'quantity': quantity_item }}
            print(vanilia_prog)
        else:
            print(vanilia_prog)
            continue
    elif input_choose == 2:
        print(vanilia_prog.replace('Entering new', 'Deliting'))
        name_item_delete = input('Enter item name to be delete  (press enter to exit): ').title()
        if name_item_delete in list(inventory.keys()):     
            if len(name_item_delete) != 0:
                check_delete = input(f'are you sure you want to delete {name_item_delete}? (y/n): ')
                if check_delete == 'y':
                    del inventory[name_item_delete]
                    print(f'{name_item_delete} has been deleted')
                else:
                    print(vanilia_prog.replace('Entering new', 'Deliting'))
                    continue
        else:
            print('this item not found')  
    elif input_choose == 3:
        print(vanilia_prog.replace('Entering new', 'Updating'))
        name_item_update = input('Enter item name to be Updated (press enter to exit): ').title()
        if name_item_update in list(inventory.keys()):    
            if len(name_item_update) != 0:
                price_item_new = int(input('Enter the new price: '))
                quantity_item_new = int(input('Enter the new quantity: '))
                inventory = inventory | {name_item_update:{'price': price_item_new, 'quantity':quantity_item_new + inventory[name_item_update]['quantity']  }}
                print(f'{name_item_update} has been updated')
                print(vanilia_prog.replace('Entering new', 'Updating'))
            else:
                print(vanilia_prog.replace('Entering new', 'Updating'))
                continue
        else:
            print('this item not found')
    elif input_choose == 4:
        print('---cheking item quantity---')
        name_item_check = input('Enter item name to be checked (press enter to exit): ').title()
        if name_item_check in list(inventory.keys()):
            if len(name_item_check) != 0:
                print(f'we have {inventory[name_item_check]["quantity"]} units')
                print('---cheking item quantity---')
            else:
                print('---cheking item quantity---')
                continue
        else:
            print('this item not found')
    elif input_choose == 5:
        print('---printing treatment information---')
        name_item_info = input('Enter item name to printing treatment information (press enter to exit): ').title()
        if name_item_info in list(inventory.keys()):
            if len(name_item_info) != 0:    
                print(f'item: {name_item_info}')
                print(f'price: {inventory[name_item_info]["price"]} EGP')
                print(f'quantity: {inventory[name_item_info]["quantity"]} units')
                print('---printing treatment information---')
            else:
                print('---printing treatment information---')
                continue
        else:
            print('this item not found')
    elif input_choose == 6:
        for name, data in inventory.items():
            print(f"{name}: [Price: {data['price']}EGP / Quantity: {data['quantity']} units]")
            print('-------------------')
    elif input_choose == 7:
        print('hava a nice day!')
        exit()


# available items
pizzas = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 150, "Chicken": 130}
burgers = {"Beef": 100, "Chicken": 80, "Bacon": 120}
drinks = {"Coke": 30, "Sprite": 25, "Fanta": 25, "Pepsi": 30} 
soups = {"Chicken Soup": 50, "Beef Soup": 60,"Mushroom Soup": 40}
desserts = {"Ice Cream": 50, "Chocolate Cake": 60,"Cheese Cake": 70}
dic_option = {'1':'pizzas', '2':'burgers', '3':'drinks', '4':'soups', '5':'desserts'}
dic_option_help = {'1':pizzas, '2':burgers, '3':drinks, '4':soups, '5':desserts}
dic_option_help_2 = {1:pizzas, 2:burgers, 3:drinks, 4:soups, 5:desserts}
total_order = []
dic_order = {}
data_order = []
check_order = False
while True:
    for index, typ in dic_option.items():
        print(f'{index}. {typ.title()}')
    number_choise = input('please, enter the number of the item you want (enter to exit): ')
    if len(number_choise) != 0 and 1<= int(number_choise) <=5:
        save_num = dic_option_help[number_choise]
        for index, (item, price) in enumerate(save_num.items()):
            print(f'{index+1}. {item}: {price} EGP')
        choose_food = input('please, enter the number of the item you want (0 to return to the previous menu): ')
        if len(choose_food) == 0:
            continue
        elif 1<=int(choose_food)<=len(dic_option_help[number_choise]):
            quantity_food = int(input('please, enter the quantity: '))

            convert_list = list(enumerate(dic_option_help[number_choise]))
            pri_name = convert_list[int(choose_food)-1][1]
            pri_price = dic_option_help[number_choise][pri_name]
            dic_order[dic_option[number_choise]] = {'Item':pri_name, 'Price(EGP)':pri_price, 'Quantity(UNIT)':quantity_food}
            check_order = True
        else:
            print('Please enter number in the menu or enter (0) to return to the previous menu, and try again!')
    elif len(number_choise) == 0:
        if check_order == True:
            print(f'{"-"*15}\n{"Your order is:"}\n{"-"*15}')
            for order, information in dic_order.items():
                total = information['Quantity(UNIT)'] * information['Price(EGP)']
                total_order.append(total)
                for i, y in dict(information).items():
                    print(f'{i}: {y}')
                print(f'Total: {total} EGP')
                print("-"*15)
            print(f'Total order is: {sum(total_order)} EGP')
        elif check_order == False:
            print('Have nice day')
        exit()    
    else:
        print('Please enter number in the menu or enter (0) to exit, and try again!')
        continue
