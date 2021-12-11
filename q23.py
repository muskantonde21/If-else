print("bank of india")
print("welcome")
atm_card=input("insert a card:")
if atm_card=="card":
    print("debit")
    print("credit card")
    print("don't remove the card till the transaction get complete")
    atm_card=input("select the card")
    if atm_card=="credit":
        print("next")
    language=input("selcet the language:")
    print("english")
    print("hindi")
    print("marathi")
    language=input("enter the lanuage:")
    if language=="english":
        print("next")
        transaction=input("choose the banking transaction:")
        print("deposit")
        print("fast cash")
        print("cash withdrawal")
        print("balance inquiry")
        print("transfer")
        print("pin charge")
        print("mini statement")
        print("other")
        transaction=input("enter the transaction :")
        if transaction=="cash withdrawal":
            print("next")
            account=input("select account")
            print("current account")
            print("saving")
            account=input("enter an account")
            if account=="saving":
                print("yes")
                password=input("enter the pin")
                if password=="4444":
                    print("next")
                    cash=int(input("enter the amount"))
                    if cash==2000:
                        print("collect your cash")
                        print("TRANSACTION COMPLETE")
                    else:
                        print("error")
                else:
                    print("incorrect")
            else:
                print("error")
        else:
            print("error")
    else:
        print("invalid")
else:
    print("invalid")
            
