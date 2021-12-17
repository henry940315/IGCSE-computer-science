password = input("enter a password  ")
admin_password = len(password)
if(admin_password >= 6 and admin_password <= 12):
    print("pass word is stored")
    print("your new password is ", password)
else:
    print("password lengh need to be in 6 ~ 12 words")