## More Dictionaries lesson 17
#
#students = {
#"Mohamed": {
#    "grades": [100, 90, 80],
#     "age": 20
#    },
# "Ahmed": {
#    "grades": [100, 95, 93],
#     "age": 21
#    },
#  "Ali": {
#    "grades": [85, 83, 87],
#     "age": 19
#    },
#   "Sara": {
#    "grades": [100, 94, 98],
#     "age": 21
#    }
#}
#print('grades mohamed is:')
#for grade in students["Mohamed"]["grades"]:
#    print(grade)
#print('-------------------')
#
#####################
#age_ali = students["Ali"]["age"]
#print(f'age ali is: {age_ali} year')
#print('-------------------')
#####################
#print('grades sara is:')
#for grade in students["Sara"]["grades"]:
#    print(grade)
#print('-------------------')
#age_sara = students["Sara"]["age"]
#print(f'age sara is: {age_sara} year')    


#students = { 
#    "Mohamed": 
#       { "grades": {  
#        "math": 100,
#        "english": 90,
#        "science": 80,
#        "arabic": 100,
#        "history": 97},
#        "school": "Codezilla"},
#
#    "Ahmed": 
#       { "grades": {  
#        "math": 100,
#        "english": 95,
#        "science": 93,
#        "arabic": 100,
#        "history": 94},
#        "school": "Codezilla"}    
#}
#grades_math = students["Mohamed"]["grades"]["math"]
#grades_english = students["Mohamed"]["grades"]["english"]
#print(f'Mohamed grades in English is:{grades_english }')
#print(f'Mohamed grades in math is:{grades_math }')
#print(f'mohamed school is: {students["Mohamed"]["school"]} school')
#
#grades_math_Ahmed = students["Ahmed"]["grades"]["math"]
#grades_science = students["Ahmed"]["grades"]["science"]
#grades_Arabic = students["Ahmed"]["grades"]["arabic"]
#print(f'Ahmed grades in math is:{grades_math_Ahmed }')
#print(f'Ahmed grades in science is:{grades_science }')
#print(f'Ahmed grades in Arabic is:{grades_Arabic }')
#
#
#restaurant_menu = {
#"Burgers": {"Beef": 100, "Chicken": 80, "Bacon": 120},
# "Pizzas": {"Cheese": 100, "Pepperoni": 120, "Veggie": 100},
#  "Drinks": {"Coke": 20, "Fanta": 20, "Sprite": 20},
#   "Desserts": {"Ice Cream": 50, "Chocolate Cake": 60,"Cheese Cake": 70},
#    "Sides": {"Fries": 30, "Onion Rings": 40, "Potato Wedges": 50}}
#
#print(f'chicken burger price is: {restaurant_menu["Burgers"]["Chicken"]}')
#print(f'veggie pizza price is: {restaurant_menu["Pizzas"]["Veggie"]}')
#print(f'coke price is: {restaurant_menu["Drinks"]["Coke"]}')
#print(f'chocolate cake price is: {restaurant_menu["Desserts"]["Chocolate Cake"]}')
#print(f'Onion Rings price is: {restaurant_menu["Sides"]["Onion Rings"]}')

students = {
    "Mohamed": {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97},
        "school": "Codezilla"
},    
    "Ahmed": {"grades": {
        "math": 100,
        "english": 95,
        "science": 93,
        "arabic": 100,
        "history": 94},
        "school": "Codezilla"
},    
    "Ali": {"grades": {
    "math": 85,
    "english": 83,
    "science": 87,
    "arabic": 100,
    "history": 90},
    "school": "Al-Azhar"
},
    "Sara": {"grades": {
    "math": 100,
    "english": 94,
    "science": 98,
    "arabic": 100,
    "history": 100},
    "school": "Al-Azhar"
    }
    
    }
grade = []
grade_ali = students['Ali']["grades"]
grade_storage = [students['Ali']["grades"][i] for i in grade_ali]
result_score = sum(grade_storage) / len(grade_storage)
print(f'score ali is: {int(result_score)}%')



    




