# Section 9: Python Functions, Loops & more Data Types
# Dictionaries & Python Tutor project number 1, 2, 3 / lesson 24 :
txt = """One of the most effective ways to reduce the friction associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a method for making cues more
obvious but you can also optimize your environment to make actions
easier
For example when deciding where to practice a new habit it is best to choose a
place that is already along the path of your daily
routine
Habits are easier to build when they fit into the flow of your life
You are more likely to go to the gym if it is on your way to work
because stopping does not add much friction to your lifestyle """

# method 1:
dict_save1 = {}
clear_txt = txt.replace('\n', '').replace(' ', '').lower()
for letter in clear_txt:
    if letter in dict_save1:
        dict_save1[letter] += 1
    else:
        dict_save1[letter] = 1
print(dict_save1)

# method 2:
dict_save2 = {}
clear_txt = ''.join(txt.split())
for letter in clear_txt.lower():
    dict_save2[letter] = dict_save2.get(letter, 0) + 1
print(dict_save2)

# method 3:
dict_save3 = {}
import re
clear_txt = re.sub(r'\s+', '', txt)
for letter in clear_txt.lower():
    dict_save3[letter] = dict_save3.setdefault(letter, 0) + 1
print(dict_save3)

# Section 9: Python Functions, Loops & more Data Types
# Dictionaries & Python Tutor project number 4 / lesson 24 :
txt = """One of the most effective ways to reduce the friction associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a method for making cues more
obvious but you can also optimize your environment to make actions
easier
For example when deciding where to practice a new habit it is best to choose a
place that is already along the path of your daily
routine
Habits are easier to build when they fit into the flow of your life
You are more likely to go to the gym if it is on your way to work
because stopping does not add much friction to your lifestyle """

convert_to_word = txt.lower().split()
dict_save = {}
for word in convert_to_word:
    dict_save[word] = dict_save.get(word, 0) + 1
for word, number in dict_save.items():
    print(f'{word}: {number}')


convert_to_word = txt.lower().split()
dict_save2 = {}
for word in convert_to_word:
    dict_save2[word] = dict_save2.setdefault(word, 0) + 1
for word, number in dict_save2.items():
    print(f'{word}: {number}')

# Section 9: Python Functions, Loops & more Data Types
# Dictionaries & Python Tutor project number 5, 6 / lesson 24 :
february_shopping_list = {
1: ['meat', 'chicken', 'chicken','chicken', 'bread', 'chocolate', 'meat'],
2: ['bread', 'milks', 'butter', 'butter', 'chocolate'], 
3: ['butter', 'meat', 'milks'],
4: ['butter', 'bread', 'nuts'],
5: ['butter', 'bread', 'chocolate', 'chocolate'], 
6: ['nuts', 'butter', 'butter','butter', 'chocolate', 'butter'],
7: ['cheese', 'milks', 'butter', 'nuts'],
8: ['cheese', 'meat', 'nuts', 'yoghurt', 'cheese'], 
9: ['chocolate', 'milks', 'milks','chocolate', 'milks', 'eggs', 'meat'],
10: ['yoghurt', 'butter', 'chocolate', 'cheese', 'butter'], 11: ['cheese', 'meat', 'yoghurt'],
12: ['eggs', 'chocolate', 'meat', 'eggs', 'butter'],
13: ['bread', 'eggs', 'yoghurt','yoghurt', 'chicken', 'chocolate'],
14: ['milks', 'meat', 'meat'],
15: ['meat', 'chicken', 'butter', 'nuts', 'nuts'], 16: ['meat', 'meat', 'chicken']
}
items_prices = {
    'meat': 250,
    'chicken': 140,
    'bread': 10,
    'chocolate': 20,
    'milks': 42,
    'butter': 75,
    'nuts': 90,
    'cheese': 65,
    'yoghurt': 25,
    'eggs': 120
}
price_tatal = []
dict_save = {}
for day, list_shopping in february_shopping_list.items():
    for item in list_shopping:
        dict_save[item] = dict_save.get(item, 0) +1
    
for item, count in dict_save.items():
    print(f'{item.title()}: {count} once')
    calc_price = count * items_prices[item]
    print(f'price for {count} {item} is: {calc_price} EGP')
    price_tatal.append(calc_price)
    print('---------')
print(f'the total price item for {len(february_shopping_list)} days earlier is: {sum(price_tatal)} EGP')

