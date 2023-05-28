# Section 9: Python Functions, Loops & more Data Types
# Dictionary Chaining Methods Project Number 01 :
products = {
    "T-shirt": {"price": 300, "quantity": 10},
    "Shirt": {"price": 250, "quantity": 20},
    "Pants": {"price": 300, "quantity": 15},
    "Shoes": {"price": 400, "quantity": 5},
    "Socks": {"price": 25, "quantity": 7},
    "Hat": {"price": 50, "quantity": 8},
    "Gloves": {"price": 50, "quantity": 10},
    "Sweater": {"price": 500, "quantity": 20},
    "Jacket": {"price": 900, "quantity": 15},
    "Coat": {"price": 1000, "quantity": 5},
    "Scarf": {"price": 110, "quantity": 2},
}

while True:
    input_user = input('enter the product name (press enter to exit): ').title()
    if input_user != '':
        show_price = products.get(input_user, {'dicroniry for help':1}).get("price", 'Not Avivable')
        show_quantity = products.get(input_user, {'dicroniry for help':2}).get("quantity", 'Not Avivable')
        user_message = f'''
        Product: {input_user}
        Price: {show_price}
        Quantity: {show_quantity}
        '''
        print(user_message)

    else:
        print('Thank for choosing codzilla!')
        exit()

# Section 9: Python Functions, Loops & more Data Types
# Dictionary Chaining Methods Project Number 02 :
patients = {
"Mohamed Hassan": {"age": 25, "disease": "Cough", "room": 1},
"Ahmed Kamal":{"age": 30, "disease": "Sore Throat", "room": 2},
"Ali Adel": {"age": 35, "disease": "Arm Fracture", "room": 3},
"Hossam Yehia": {"age": 40, "disease": "ACL", "room": 4}
}
while True: 
    input_user = input('enter the patient name: ').title()
    if len(input_user) != 0:
        check = patients.setdefault(input_user, {"age": 'not avivable', "disease": 'not avivable', "room": 'not avivable'})
        print(f'patient: {input_user}')
        for info in patients[input_user].keys():
            show_info = patients.get(input_user, {'help':1}).get(info, 'not avivable')
            print(f'{info.title()}: {show_info}')
    else:
        print('Have a nice day!')
        exit()


# Section 9: Python Functions, Loops & more Data Types
# Dictionary Chaining Methods Project Number 01 :
# Section 9: Python Functions, Loops & more Data Types
# Dictionary Chaining Methods Project Number 04 :
students = {
    "Mohamed Hassan": {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97}
},
"Ahmed Kamal": {"grades": {
    "math": 100,
    "english": 95,
    "science": 93,
    "arabic": 100,
    "history": 94}
},
"Ali Adel": {"grades": {
    "math": 85,
    "english": 83,
    "science": 87,
    "arabic": 100,
    "history": 90}
},
"Hossam Yehia": {"grades": {
    "math": 100,
    "english": 94,
    "science": 98,
    "arabic": 100,
    "history": 100}
} }
while True: 
    input_name = input('enter student name(press enter to exit): ').title()
    
    if len(input_name) != 0:
        print(f'Student: {input_name}')
        check_name = students.get(input_name, {}).get("grades", 'No grades avivable')
        if check_name != 'No grades avivable':
            for subject, grade in check_name.items():
                print(f'{subject}: {grade}')
            print('-'*15)
        else:
            print(check_name)

    else:
        print('have a nice day!')
        exit()

