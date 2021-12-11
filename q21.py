user=input("enter the email address or phone number:-")
if user=="muskantonde@gmail.com":
    print("enter")
elif user=="enter your user id":
    print("enter")
    password=input("enter the password:")
    if password=="enter your password":
        print("login")
    else:
        print("forgot password")
else:
    print("incorrect email or number")

id=input("creat new account")
print("enter")
name=input("enter the name")
if name=="muskan":
    print("next")
    DOB=input("enter the date")
    if DOB=="31/10/2003":
        print("next")
        gender=input("select the gender")
        print("FEMALE")
        print("MALE")
        print("customer")
        gender=input("enter the gender:")
        if gender=="female:":
            print("next")
            choose_password=input("enter the password:")
            if choose_password=="12345678":
                print("re-enter password:")
                password=input("re-enter password:")
                if password=="12345678":
                    print("login")
                else:
                    print("can't recognise")
            else:
                print("can't recognise")
        else:
            print("can't recognise")
    else:
        print("can't recognise")
else:
    print("can't recognise")