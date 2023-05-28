## Section 9: Python Functions, Loops & more Data Types
# lesson 3 - While Loops (Strong Password Project)
#-------------------------------------
# !password project PART 1:
#? call up libery random and string : 
import random
import string

#? use method string
pass_word = string.punctuation + string.ascii_letters + string.digits

#? use while loop and choise word password if user enter len password : 
len_pass = int(input('Please Enter your password length: '))
password_user = ''

while len(password_user) < len_pass: 
    choise_word = random.choice(pass_word)
    
    password_user += choise_word
# ! print password for user :
print(f'Your password ready: {password_user}')   


## Section 9: Python Functions, Loops & more Data Types
# lesson 3 - While Loops (Strong Password Project)
#-------------------------------------
# !password project PART 2:
#? call up libery random and string : 
import random
import string

#? use method string
pass_word = string.punctuation + string.ascii_letters + string.digits

#? use while loop and choise word password if user enter len password : 
len_pass = int(input('Please Enter your password length: '))
password_user = ''

while len(password_user) < len_pass: 
    choise_word = random.choice(pass_word)
    
    password_user += choise_word
    if pass_word[:]:
# ! print password for user :
        print(f'Your password ready: {password_user}')   

