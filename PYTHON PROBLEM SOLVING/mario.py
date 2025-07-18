# Write a program that build a Mario pyramid like below:
def mario_pyramid(num):
    stars = 1
    spaces = num-1
    for i in range(num):
        print(" "*spaces+"*"*stars)
        stars+=1
        spaces-=1
# ==============================================================

def pyramids_with_list() :
    list=[]
    num_of_row = int(input(" Enter Numbers of Pyramids Number of : "))
    for i in range(1,num_of_row+1) :
        list.append(" ")


    for i in range(1,num_of_row+1):
        list.append("*")
        list.remove(' ')
        print(list)
