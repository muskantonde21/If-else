letter=input("enter the letter")
if letter>="A" or letter<="Z":
    special_chac=input("enter the special chacracter")
    if special_chac=="@" or "$" or "#":
        num=int(input("enter the number"))
        if num>1:
            print(letter+special_chac+str(num))
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")
