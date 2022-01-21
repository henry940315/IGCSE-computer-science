
a = 0
while(a < 1000000000):

    password = {"Henry":20050315, "Amy":12345678, "Mike":99887766}

#get the name from the dictionary
    for name in password:
        print()
    



    user_name = input("Enter your user name    ")
#if the name of input did not have in the dictionary, registe it
    if(user_name != name or user_name != registe):
        print("You are not registed, please registed")
        registe = input("Enter a name   ")
        registe_password = int(input("Enter a 8 numbers password      ") )
        print("your new account name: ",registe,"password is ",registe_password)
        registe = [registe_password]

    elif(user_name==user_name):
        get_someone = password.get(user_name)

        user_enter_password = int(input("Enter you password   ") )


        if(user_enter_password == get_someone):
            print("The password is correct")
        else:
            print("Password is not correct")
        

    a = a + 1





