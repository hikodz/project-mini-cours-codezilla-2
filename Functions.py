# Lesson 30 - Introduction to Functions |PROJECT part 1
def greet_user(name):
    print(f'Welcome {name.title()} at Python Course\nEnjoy your Learning Journey')
input_name = input('Please enter your name: ')
greet_user(input_name)
print('-----------------')

# Lesson 30 - Introduction to Functions |PROJECT part 2
def text_user(text):
    print(f'your text reverse: {text[::-1]}')
input_text = input('Please enter your text: ').lower()
text_user(input_text)

pizzas = {
    "Margherita": 120,
    "Pepperoni": 200,
    "Hawaiian": 150,
    "Meat Lovers": 250,
    "Mushroom": 140,
}
for pizza_name, price_item in pizzas.items():
    def info_pizzas(name, price):
        print(f'{name} Pizza: {price} EGP')
    info_pizzas(pizza_name, price_item)

def print_employees_info(name= None, age= None, salary= None, section = None):
    print(f"Name: {name.title()}")
    print(f"Age: {age}")
    print(f"Salary: {salary}")
    print(f"section: {section}")

# 1.
print_employees_info("Mohamed ahmed", 25, 10_000)
# 2.
print_employees_info("hassan Ali", 33, 15_000) 
# 3.
print_employees_info(age=30, name="Ali Hassan", salary=20_000) 
# 4.
print_employees_info("Ahmed Mohamed", 15_000, 35) 
# 5.
print_employees_info("Hazem Khaled", salary=15_000)
# 6.
print_employees_info(age = 25, name = "Hamed Ali", salary= 14_000)
# 7.
print_employees_info("Mohamed khedr", salary=13_000, age=25, section="IT")

import random
def print_students_info(name='hamada', age=random.randint(18, 60) , city = "Cairo", school = "Codezilla"):
    print(f"Name: {name.title()}")
    print(f"Age: {age}")
    print(f"City: {city.title()}")
    print(f"School: {school.title()}")
# Print the following Information for each Student:
print_students_info('ahmed mohamed', 25)
print_students_info('mohamed ahmed', 33, school = 'al-azhar')
print_students_info('ali hassan', 30, 'alexendaria')
print_students_info('hazem khaled', 35, 'new york', 'khaled ibn al-walid')
print_students_info('hamed ali', 25, 'tanta', "al durra")