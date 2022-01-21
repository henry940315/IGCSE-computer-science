

a =  0
while(a < 10000000000000000):



    list_of_name = ["Amy","Charlie","Mars","David","Leon"]
   
    while(a>=1):     
    
        print("the list:  ",list_of_name)
        ask = int(input("Do you want to remove name or add name?  If you want to add name, please press 1, if you want to remove name, please press 2    ")) 
        if(ask == 1):
            want_add = input("Which name do you want to add       ")
            list_of_name.append(want_add)

        elif(ask == 2):
            want_remove = input("Which name do you want to remove       ")  
            list_of_name.remove(want_remove)
        else:
            print("please enter the correct number")


        print(list_of_name)
    
    a = a + 1



