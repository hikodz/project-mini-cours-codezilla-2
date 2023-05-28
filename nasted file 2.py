## Section 9: Python Functions, Loops & more Data Types
## Nested Loops project part 1 : file 2 : 
words = [
'each', 'those', 'feel', 'seem', 'high', 'place',
'little', 'world', 'very', 'still',
'nation', 'hand', 'life', 'tell', 'write', 'become',
'here', 'show', 'house', 'both',
'between', 'need', 'mean', 'call', 'develop', 'under',
'last', 'right', 'move', 'thing',
'general', 'school', 'never', 'same', 'another',
'begin', 'while', 'number', 'part',
'turn', 'real', 'leave', 'might', 'want', 'point',
'form', 'child', 'small', 'since',
'against', 'late', 'home', 'interest', 'large',
'person', 'open', 'public', 'follow',
'during', 'present', 'without', 'again', 'hold',
'codezilla', 'govern', 'around',
'head', 'consider', 'word', 'program', 'problem',
'however', 'lead', 'system',
'order', 'plan', 'keep', 'face', 'group', 'play',
'stand', 'increase',
'early', 'course', 'change', 'help', 'line',
'possible', 'fact', 'down'
]
search_word_user = input("enter word: ")
check = True
for word in words:
    if search_word_user.lower() in words:
        print("this word exists in list")
        check = False
        break
if check == True:
    print("this word not exists in list")    

## Section 9: Python Functions, Loops & more Data Types
## Nested Loops project part 3 : file 2 : 
numbers = [
-500, -694, -762, -445, -348, -361, -758, -594,
-954, -861, -610, -549, -336, -400, -600, -836, -671, -573,
-555, -390, -450, -811, -849, -870, -815, -694, -951, -588,
-484, -609, -674, -411, -408, -498, -649, -541, -441, -839,
-567, -898
]

list_convert = []
for number in numbers:
    number *= -1
    list_convert.append(number)
print(list_convert)    
## Section 9: Python Functions, Loops & more Data Types
## Nested Loops project part 4 : file 2 : 
lst_words = [
['have', 'that', 'they', 'with', 'this', 'from',
'which', 'would', 'will', 'there', 'make', 'when', 'more',
'other', 'what', 'time', 'about', 'than', 'into', 'could'],
[ 'state', 'only', 'year', 'some', 'take', 'come', 'these',
'know', 'like', 'then', 'first', 'work', 'such', 'give',
'over', 'think', 'most', 'even', 'find', 'also', 'after',
'many', 'must', 'look', 'before', 'great', 'back', 'through',
'long'],
[ 'where', 'much', 'should', 'well', 'people', 'gouda', 'just',
'because', 'good', 'each', 'those', 'feel', 'seem', 'high',
'place', 'little', 'world', 'very', 'still', 'nation', 'hand',
'life', 'tell', 'write', 'become', 'here', 'show', 'house',
'both', 'between', 'need', 'mean', 'call', 'develop', 'under',
'last', 'right', 'move', 'thing'],
['general', 'school', 'never', 'same', 'another', 'begin',
'while', 'number', 'part', 'turn', 'real', 'leave', 'might',
'want', 'point', 'form', 'child', 'small', 'since', 'against',
'late', 'home', 'interest', 'large', 'person', 'open',
'public', 'follow', 'during', 'present', 'without', 'again',
'hold', 'codezilla', 'govern', 'around', 'head', 'consider',
'word', 'program', 'problem', 'however', 'lead', 'system'],
['order', 'plan', 'keep', 'face', 'group', 'play', 'stand',
'increase', 'early', 'course', 'change', 'help', 'line',
'possible', 'fact', 'down']
]
lis_letters = []
for lis in lst_words:
    for word in lis:
        for letter in word:
            lis_letters.append(letter)
print(f'the number of occurrences of the letter "a" is: {lis_letters.count("a")}')
#print(f'the number of occurrences of the letter "e" is: {lis_letters.count("e")}')               

### Section 9: Python Functions, Loops & more Data Types
### Nested Loops project part 2 : file 3: 
words = [
'have', 'that', 'they', 'with', 'this', 'from',
'which', 'would', 'will', 'there', 'make', 'when', 'more',
'other', 'what', 'time', 'about', 'than', 'into', 'could',
'state', 'only', 'year', 'some', 'take', 'come', 'these',
'know', 'like', 'then', 'first', 'work', 'such', 'give',
'over', 'think', 'most', 'even', 'find', 'also', 'after',
'many', 'must', 'look',
'before', 'great', 'back', 'through', 'long', 'where', 'much',
'should', 'well', 'people', 'gouda', 'just', 'because', 'good',
'each', 'those', 'feel', 'seem', 'high', 'place', 'little',
'world', 'very', 'still', 'nation', 'hand', 'life', 'tell',
'write', 'become', 'here', 'show', 'house', 'both', 'between',
'need', 'mean', 'call', 'develop', 'under', 'last', 'right',
'move', 'thing', 'general', 'school', 'never', 'same',
'another', 'begin', 'while', 'number', 'part', 'turn', 'real',
'leave', 'might', 'want', 'point', 'form', 'child', 'small',
'since', 'against', 'late', 'home', 'interest', 'large',
'person', 'open', 'public', 'follow', 'during', 'present',
'without', 'again', 'hold', 'codezilla', 'govern', 'around',
'head', 'consider', 'word', 'program', 'problem', 'however',
'lead', 'system', 'order', 'plan', 'keep', 'face', 'group',
'play', 'stand', 'increase', 'early', 'course', 'change',
'help', 'line', 'possible', 'fact', 'down'
]

lis_uppercase = []
for word in words:
   word_upper = word.upper()
   lis_uppercase.append(word_upper)
print(lis_uppercase)   
### Section 9: Python Functions, Loops & more Data Types
### Nested Loops project part 4 : file 3: 
numbers = [
-588, -479, -713, -701, -885, -578, -835, -466, -
935, -665, -360, -837, -389, -367, -454, -668, -907, -822, -
541, -680, -405, -330, -625, -916, -331, -876, -689, -753, -
810, -648, -787, -952, -718, -401, -502, -699, -533, -450, -
580, -725
]

number_first = numbers[0]
for number in numbers:
    if number < number_first:
        number_first = number
print(f'the smallest number is: {number_first}')      
#### Section 9: Python Functions, Loops & more Data Types
#### Nested Loops project part 5 : file 3: 


numbers = [-500, -694, -762, -445, -348, -361, -758, -594, -
954, -861, -610, -549, -336, -400, -600, -836, -671, -573, -
555, -390, -450, -811, -849, -870, -815, -694, -951, -588, -
484, -609, -674, -411, -408, -498, -649, -541, -441, -839, -
567, -898]

number_first = numbers[4]
for number in numbers:
    if number%2 !=0 and number < number_first:
        number_first = number 
print(f'the smallest odd number is: {number_first}')    
### Section 9: Python Functions, Loops & more Data Types
### Nested Loops project part 6 : file 3: 


sentence = """Python is a widely used high-level
general-purpose interpreted dynamic programming language
Its design philosophy emphasizes code readability and its
syntax allows programmers to express concepts in fewer lines of
code
than possible in many other languages
The language provides constructs intended to enable clear
programs on both a small and large scale
"""

list_sentence = list(sentence)
##len_names = [len(word)for word in sentence]
print(list_sentence)