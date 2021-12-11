username=input("enter the name")
password=int(input("enter the password"))
if username=="muskan":
    if password==12345678:
        print("your login is successful")
    else:
        print("incorrect password")
elif username!="muskan"and password!="12345678":
    print("both are incorrect,creat new mail id")
    username=input("enter the username")
    password=int(input("enter the password"))
    print("your account is created")
else:
    print("incorrect username")





