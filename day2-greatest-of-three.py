num6=int(input(" Enter the first number:"))
num7=int(input(" Enter the secnd number "))
num8=int(input("Enter the third number : "))
if( num6>num7 and num6>num8):
    print(num6,"is greater")
elif( num7>num8 and num7>num6):
    print(num7,"is greater")
elif(num8>num6 and num6>num8):
    print( num8,"is greater")
else:
    print("Invalid option")
