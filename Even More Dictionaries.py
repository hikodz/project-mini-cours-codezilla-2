pizzas = {
        "Margherita": 100,
        "Pepperoni": 120,
        "Meat Lovers": 150,
        "Chicken": 130,
        "Cheese": 100,
        "Veggie": 120,
        "Hawaiian": 150
}
print('pizza avivable:')
for index, (pizza, price) in enumerate(pizzas.items()):
    print(f'{str(index+1).zfill(2)}. {pizza}: ${price}')

menu = {
    "Cheese pizza": 100,
    "Veggie pizza": 120,
    "Hawaiian pizza": 150,
    "Coke": 30,
    "Sprite": 25,
    "Fanta": 25,
    "Pepsi": 30
}
menu.update({'Ice Cream': 30})
menu.update({'Chocolate Cake ':60})
menu.update({'Cheese Cake':70})
menu.update({'Brownie':40})
menu.update({'Donut':30})
print('desserts avivable:')
for dessert, price in menu.items():
    print(dessert, price, sep=':')


menu = {
    "Cheese pizza": 100,
    "Veggie pizza": 120,
    "Hawaiian pizza": 150,
    "Coke": 30,
    "Sprite": 25,
    "Fanta": 25,
    "Pepsi": 30
} 

for food, price in menu.items():
    percentage_of_item = (price / 100) * 20
    menu[food] += int(percentage_of_item)
print(menu)

drinks = {
    "Latte": 30,
    "Coke": 30,
    "Sprite": 25,
    "Fanta": 25,
    "Pepsi": 30,
    "Tea": 20,
    "Coffee": 25,
    "Orange Juice": 30,
    "Mango Juice": 30
}
soda = ["Coke", 'Sprite', 'Fanta', 'Pepsi']
for drink, price in drinks.items():
    if drink in soda:
        print(f'{drink}: {price}')


pizzas = {
    "Margherita": 100,
     "Pepperoni": 120,
      "Meat Lovers": 150,
       "Chicken": 130
       }
check = True
sq_user = input("please enter your order: ").title()
for pizza, price in pizzas.items():
    if sq_user == pizza:
        check = False
        print(pizza, price, sep=': ')
if check == True:
    print('Sorry your order not found')      



schools = {
            "Codezilla School":
{'1100':"Mohamed Gouda",
 '1101':"Islam Hesham",
  '1102':"Ayman Mohamed",
   '1103':"Ahmed Khaled"},

            "Al Dorra School":
{'2100':"Ahmed Hassan",
 '2101':"Mahmoud Ali",
 '2102':"Adham Wael",
  '2103':"Khaled Ali"},

            "Mostafa Kamel School":
{'3105':"Hazem Ahmed",
 '3106':"Omar Mohamed",
 '3107':"Hussein Kamal",
  '3109':"Ali Ahmed"}
}
input_search = input('Please enter name or number student: ')
for school, info in schools.items():
    for code, name in info.items():
        if input_search == code or input_search.title() == name:
            print(school)  


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
"Sara Ahmed": {"grades": {
    "math": 100,
    "english": 94,
    "science": 98,
    "arabic": 100,
    "history": 100},
    "school": "Al-Azhar"
    }
}
check_els = True
input_useer = input('please, enter the name of the student: ').title()
list_score = []
for name, info in students.items():
    if input_useer == name:
        check_els = False
        print(f'{name} got the followin grades:')
        for subject, grade in info["grades"].items():
            print(subject, grade, sep=': ' )
            list_score.append(grade)
        score = sum(list_score) / len(list_score)
        print(f'{name} total percentage is {score:.2f}%')
        print("-"*25)

if check_els == True:
    print('sorry, ew don\'t have info about this students')