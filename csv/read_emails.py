

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
with open(r"C:\Users\Youss\OneDrive\Desktop\Emails.csv.csv", "r") as upload:
    reader = csv.reader(upload)
    header = next(reader)  

    for row in reader:
        if len(row) > 3:
            email = row[3]
            emails.append(email)

print("==========================================================================================================")
validemails = list(filter(validemail, emails))
print(validemails)
print("==========================================================================================================")
domains = list(map(lambda x: x.split('@')[1], validemails))
print(domains) 
print("==========================================================================================================")
unique_domains = set(domains)
print(unique_domains)
