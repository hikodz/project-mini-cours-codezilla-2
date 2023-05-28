#اكسب الصلاة على خير الخلق رسول الله محمد صلى الله عليه و سلم
#------------------------------------------------------------|
## Section 9: Python Functions, Loops & more Data Types
## Lesson 7 - Range function part 2  // project #! part 1 :aaaa
#----------------------------------------------------------
## Print the total of numbers between 0 to 100:
#total = 0
#for i in range(0, 101, 1):
#    total += i
#print(f'The result is: {total}')
#----------------------------------------------------------
## Print the total of numbers between 70 to 160:
#total = 0
#for i in range(70, 161, 1):
#    total += i
#print(f'The result is: {total}')
#----------------------------------------------------------
## Print the total of even numbers between 30 to 470:
#total = 0
#for i in range(30, 471, 2):
#    total += i
#print(f'The result is: {total}')
#----------------------------------------------------------
## Print the total of numbers that are divisible by 3 and between 1 to 1000:
#total = 0
#for i in range(1, 1001, 1):
#    if i % 3 == 0 :
#        total += i
#print(f'The result is: {total}')
#----------------------------------------------------------
## Make a program that calculate the average of 
## the second highest and second lowest numbers 
## that are between 452 and 983 and are divisible by 5 and 7:
#list_real = []
#for i in range(452, 983, 1):
#    if i % 5 == 0  and  i % 7 == 0:
#        list_real.append(i)
#
#average_max_min = (list_real[1]+ list_real[-2]) / 2  
#print(f'Your average is: {average_max_min}')

#اكسب الصلاة على خير الخلق رسول الله محمد صلى الله عليه و سلم
#------------------------------------------------------------|
## Section 9: Python Functions, Loops & more Data Types
## Lesson 7 - Range function part 2  // project #! part 2 :
#----------------------------------------------------------
# Sum the even numbers between 28 and 928 in at least 3 different ways:
# method 1 use for in loop :
#total = 0 
#for i in range(28, 929, 2):
#    total += i
#print(f'Your result is: {total}') 
#
## method 2 use for in loop :
#list_num = []
#for i in range(28, 929, 2):
#    list_num.append(i)
#total = sum(list_num)    
#print(f'Your result is: {total}')
#
## method 4 use while loop :
#number_min = 26
#total = 0
#while number_min < 928:
#    number_min += 2
#    if number_min % 2 ==0:
#        total += number_min
#print(f'Your result is: {total}') 
#اكسب الصلاة على خير الخلق رسول الله محمد صلى الله عليه و سلم
#------------------------------------------------------------|
## Section 9: Python Functions, Loops & more Data Types
## Lesson 7 - Range function part 2  // project #! part 3 :
#------------------------------------------------------------|

#fruits = ['apple', 'banana', 'orange', 'grape', 'mango']        
#
#print("Available fruits:")
#number_ranking = 0
#
#for i in fruits:
#    number_ranking += 1
#    print(f'{number_ranking}. {i}')
#

# a list of pizzas
pizzas = ['Margherita', 'Pepperoni', 'Super Supreme', 'Hawaiian', 'Meat Lovers', 'Cheese Lovers']

intro_pizza = '''
Welcome to Codezilla Pizza!
We have the following pizzas:
--------------------------------
1. Margherita
2. Pepperoni
3. Super Supreme
4. Hawaiian
5. Meat Lovers
6. Cheese lovers
'''
end_choose = '''Thank for choosing codezilla pizza!
Please, enjoy your time
'''
print(intro_pizza)
list_help = [0]
for i in list_help:
    choose_pizza = int(input('Enter the number of the pizza you want to order: '))
    pizza_number = input('Enter the number of pizzas you want: ')
    print('-'*30)
    print(end_choose)
print(f'while we get {pizza_number} {pizzas[choose_pizza-1]} ready for you') 
   

     