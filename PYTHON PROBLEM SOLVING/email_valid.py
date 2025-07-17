#You are given a list of email addresses in the format username@domain.
# Your goal is to use the map() function with a lambda to extract only the domain part from each emai
email=["ali@yahoo.com","youusef23@gmail.com","ahmed333@icloud.com"]
def domains(email):
     domains = list(map(lambda email: email.split('@')[1], email))
     return domains
# ============================================================================== 
#  proceed to ask him for his email and print all this data(Bonus) check if it is 
# a valid email or no with try and except

def validemail(email):
 try:
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        
        if username and domain:
            if "." in domain:
                x,*y=domain.split('.')
                if x and y:
                    return True
                else : 
                    return False
            else :
                return False
        else : 
            return False
    else :
        return False
 except:
     print('invalid email')

#     # ==============================================================
