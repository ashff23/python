import mario 
import letters
import lists
import Dictionary
import email_valid
email=[
     "ali@gmail-com",
     "sara@yahoo.com",
     "mohamed@outlook.com",
     "noha@iti.gov.eg"
]
print(email_valid.domains(email))

print ('##############')

user_email=input('enter you email:          : ')
if email_valid.validemail(user_email):
     print("valid")
else:
     print("invalid")

print('------------------------------------------------------')

x=input("enter the vowels  : ")
letters.count_vowels(x)

print ('##############')

x=input("enter the word with letter i : ")
print(letters.count_i(x))

print ('##############')

number=int(input('enter a number  '))
lists.Multi_Table(number)

print('------------------------------------------------------')
# user = [{"name":"jack","pass":"2345"},{"name":"rose","pass":"3344"}]
userInput=input("enter your name:  ")
Dictionary.check_user_fun(userInput)

print('------------------------------------------------------')

x=int(input("enter ur number :"))
mario.mario_pyramid(x)

print ('##############')

mario.pyramids_with_list()

print('------------------------------------------------------')

lists.sort_numbers()

print ('##############')

print(lists.generate_multi())

print('------------------------------------------------------')
