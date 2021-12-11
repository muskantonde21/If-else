app=input("enter the app:")
if  app=="facebook":
    print("welcome to the fecebook")
    account=input("enter the account:")
    if account=="new" or account=="old":
        print("yes")
        name=input("enter the name")
        if name>="a" and name<="z"or name>="A" and name<="Z":
            print(name)
            name=input("enter the last name")
            if name>="a" and name<="z" or name>="A" and name<="Z":
                print(name)
                date=input("enter the date")
                if date>="0" and date<="9" or date=="/":
                   print(date)
                   gender=input("enter the gender")
                   if gender=="female" or gender=="male" or gender=="other":
                        print(gender)
                        contact=input("enter the contact number")
                        if contact>="0" or contact<="9":
                            print(contact)
                            password=input("enter the password")
                            if password>="0" and password<="9" or password>="a" and password<="z" or password>="A" and password<="Z":
                                print(password)
                                profile=input("enter the your profile")
                                if profile=="gallery" or profile=="take a new photo":
                                    print(profile)
                                    email=input("enter the your email")
                                    if email>="a" and email<="z" or email>="A" and email<="Z" or email>="0" and email<="9":
                                        print("yes")
                                        account=input("enter the fecebook account")
                                        if account =="successfuly":
                                           print("well done")
                                           satisfying=input("enter the your satisfection")
                                           if satisfying =="satisfyde":
                                              print("yes")
                                           else:
                                                 print("no")
                                        else:
                                            print("thank you")
                                    else:
                                         print("no")
                                else:
                                     print("your multiple choice")
                            else:
                                 print("this is possword is wrong")
                        else:
                             print("hide my contact number")
                   else:
                        print("real")
                else:
                    print("wrong")
            else:
                print("my last name is incorrect")
        else:
             print("my first name is incorrect")
    else:
         print("no")
else:
     print("wrong")

print("your facebook account is successfull")
