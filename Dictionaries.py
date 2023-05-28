#
storage_data = {
 "Apple" : 20,
 "Banana" : 15,
 "Orange" : 10,
 "Strawberry" : 30,
 "Mango" : 25
}
print(storage_data)


grade_student = {
    'Mohamed Hassan' : 83,
    'Ahmed Khaled' : 97,
    'Ali Hamed' : 75,
    'Mahmoud Samir' : 89
    }
print(grade_student)

drink = {
    'Coke': 10,
    'Sprite' : 8,
    'Fanta' : 8,
    'Pepsi' : 10}
print(drink)

ranking_grades = { 
    1 : 'Mohamed Ahmed',
    2 : 'Ahmed Khaled',
    3 : 'Ali Hamed',
    6 : 'Mahmoud Samir',
    8 : 'Ahmed Hassan'
    }

grades = {
    ("Ahmed", "Hassan"): 87,
    ("Hossam", "Ali"): 90,
    ("Mohamed", "Kamel"): 74,
    ("Ali", "Hamed"): 100,
    ("Ahmed", "Khaled"): 95
}
print(grades)

pizzas = {
        "Margherita": 100,
        "Pepperoni": 120,
        "Meat Lovers": 150,
        "Chicken": 130,
        "Cheese": 100,
        "Veggie": 120,
        "Hawaiian": 150,
}
for i in pizzas:
    print(f'{i}: ${pizzas[i]}')

drinks = {
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30,
"Tea": 20,
"Coffee": 25,
"Orange Juice": 30,
"Mango Juice": 30  
}      


for i in drinks:
    print(f'{i}: ${drinks[i]}')

menu = {
"Cheese pizza": 100,
"Veggie pizza": 120,
"Hawaiian pizza": 150,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30
}
menu['Ice Cream'] = 30 
menu['Chocolate Cake'] = 60
menu['Cheese Cake'] = 70
menu['Brownie']= 40
menu['Donut'] = 30
print(menu)
for i in menu:
    print(f'{i}: ${menu[i]}')

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
for drink in drinks:
    print(drink)