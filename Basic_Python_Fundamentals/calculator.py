a=float(input("Enter the value for a: "))
b=float(input("Enter the value for b: "))

print("Press 1 for Addition\nPress 2 for Multiplication\nPress 3 for Subtraction\nPress 4 for Divition\nPerss 5 for Modulation")
ch=int(input("Enter your choice: "))

if ch==1:
    c=a+b
    print(c)
elif ch==2:
    c=a*b
    print(c)
elif ch==3:
    c=a-b
    print(c)
elif ch==4:
    c=a/b
    print(c)
elif ch==5:
    c=a%b
    print(c)
else:
    print("Invalid choice....Please try again!!!")        