   
def check_user_fun(userinput):
 user = [{"name":"jack","pass":"2345"},{"name":"rose","pass":"3344"}]

 for e in user:
    if e["name"] ==userinput:
        userPass=input("enter ur pass:  ")
        if e ["pass"] ==userPass:
            print("ur pass correct")
            break
        else:
            print("incorrect password")
        break
    
    else:
        continue
 else:
    print("not found")