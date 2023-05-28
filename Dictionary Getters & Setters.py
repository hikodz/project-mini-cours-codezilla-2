#Section 9: Python Functions, Loops & more Data Types
# Dictionary Getters & Setters project number 1:
# available treatments
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

while True:
    input_user_search = input('Enter treatment name(press enter to exit): ').title()
    if input_user_search != "":
        x = inventory.get(input_user_search, 'Not Avivable')

        if x != 'Not Avivable':
            print(f'Item: {input_user_search}')
            for key, value in x.items():
                print(f'{key.title()}: {value}')
        else:
            print(x)
    else:
        print('Have a nice day!')
        exit()
    
#Section 9: Python Functions, Loops & more Data Types
# Dictionary Getters & Setters project number 2:
employees = {
"Mohamed Hassan": {"age": 25, "salary": 5000, "department":"HR"},
"Ahmed Kamal": {"age": 30, "salary": 6000, "department":"IT"},
"Ali Adel": {"age": 35, "salary": 7000, "department":"IT"},
"Hossam Yehia": {"age": 40, "salary": 8000, "department":"IT"} 
}

while True:
    input_user = input('Enter the employee name (Press enter to exit): ').title()
    if input_user != "":
        use_get = employees.get(input_user, 'Not Avivable')
        if use_get != 'Not Avivable':
            print(f'Employee: {input_user}')
            for key, value in use_get.items():
                print(f'{key.title()}: {value}')
        else:
            print(use_get)
    else:
        print('Have a nice day!')
        exit()

# Section 9: Python Functions, Loops & more Data Types
# Dictionary Getters & Setters project number 4:
pharmacy_prices = {
    "panadol": 32,
    "cold free": 25,
    "omega 3": 45,
    "fuciden": 37,
    "augmentin": 50,
    "zinc": 20,
    "vitamin c": 15
}
while True:
    input_user = input('enter the  names of treatments separated by a coma (Press Enter to Exit):  \n')
    if len(input_user) != 0:   
        convert_for_check = input_user.split((', '))
        print('-'*20)
        for name in convert_for_check:
            check_name = pharmacy_prices.get(name, 'Not Avivable')
            print(f'{name.title()}: {check_name}')
    else:
        print('have a nice day!')
        exit()
    
