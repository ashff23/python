#  Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    counter = 0
    for i in text:
        if i in vowels:
            counter += 1
    print(counter)
x=input("enter the word : ")
count_vowels(x)
# ===============================================================================================
#   Write a program that prints the locations of "i" character in any string you added.
def count_i(letter):
    count = 0
    for e in range(len(letter)):
        if letter[e] == "i":
            count += 1
    return count

x=input("enter thw word:")
print(count_i(x))
# =============================================================================
#  Write a program that generate a multiplication table from 1 to the number passed.
def Multi_Table(number):
    for i in range(number+1):
        for d in range(1,i+1):
            print(f"{i}x{d}= {i*d}")
    print()       

number=int(input('enter a number  '))
print(Multi_Table(number))
# ====================================================================================
