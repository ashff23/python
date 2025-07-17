
import csv

def validemail(email):
    if '@' in email and '.' in email:
        try:
            username, domain = email.split('@')
            if username and domain:
                x, *y = domain.split('.')
                if x and y:
                    return True
        except:
            pass
    return False

emails = []
with open(r"C:\Users\Youss\OneDrive\Desktop\Emails.csv.csv", "r") as z:
    reader = csv.reader(z)
    header = next(reader)  

    for i in reader:
        if len(i) > 3:
            email = i[3]
            emails.append(email)

print("=================================================================================================================================================")
validemail = list(filter(validemail, emails))
print(validemail)
print("=====================================================================================================================================================")
domain= list(map(lambda x: x.split('@')[1], validemail))
print(domain) 
print("=================================================================================================================================================")
uniquedomain = set(domain)
print(uniquedomain)
