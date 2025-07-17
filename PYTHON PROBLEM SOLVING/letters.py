#  Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    counter = 0
    for i in text:
        if i in vowels:

            counter += 1
    print(counter)

# ===============================================================================================
#   Write a program that prints the locations of "i" character in any string you added.
def count_i(letter):
    count = 0
    for e in range(len(letter)):
        if letter[e] == "i":
            count += 1
    return count
# =============================================================================

  



