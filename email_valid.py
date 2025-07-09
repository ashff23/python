#You are given a list of email addresses in the format username@domain.
# Your goal is to use the map() function with a lambda to extract only the domain part from each emai
def domains(mail):
    domains = list(map(lambda email: email.split('@')[1], mail))
    return domains
# print(domains())
# ============================================================================== 
#  proceed to ask him for his email and print all this data(Bonus) check if it is 
# a valid email or no with try and except
def valid_mails(email):
    try:
      if '@' in email and '.' in email:
        username, domain = email.split('@')
        if username and domain:
            x,y=domain.split('.')
            if x and y:
               return True
    except:
        return False
    # ==============================================================
    def filtring_emails(list_of_emails ):
        return list(filter(valid_mails,list_of_emails ))