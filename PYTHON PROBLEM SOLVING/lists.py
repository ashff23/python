# Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display 

def sort_numbers():
    x = []
    for i in range(5):
        z = int(input("Enter a number: "))
        x.append(z)
    
    print("Ascending order:", sorted(x))
    print("Descending order:", sorted(x, reverse=True))
# ==============================================================
#  Write a program that generate a multiplication table from 1 to the number passed
def generate_multi():
    l = []
    x = int(input('Enter a number: '))
    
    for i in range(x + 1):
        w = []
        for d in range(1, i + 1):
            w.append(i * d)
        l.append(w)
    return l 
# ==================================================================
#  Write a program that generate a multiplication table from 1 to the number passed.
def Multi_Table(number):
    for i in range(number+1):
        for d in range(1,i+1):
            print(f"{i}x{d}= {i*d}")
