# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# if num1>=num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)


