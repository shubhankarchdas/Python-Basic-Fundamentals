name=input("Enter your name : ");
s1=int(input("Enter the marks for subject1: "));
s2=int(input("Enter the marks for subject2: "));
s3=int(input("Enter the marks for subject3: "));
s4=int(input("Enter the marks for subject4: "));
s5=int(input("Enter the marks for subject5: "));
total=s1+s2+s3+s4+s5; 
per= float(total)/5;
print(per)
if per >= 90 and per <=100:
    print('AA')
elif per>= 80 and per <=100:
    print('A')
elif per>=70 and per <=100:
    print('B')
elif per>=60 and per <=100:
    print('C')
elif per>=50 and per <=100:
    print('D');
elif per >=45 and per <=100:
    print('E');
elif per<45 and per <=100:
    print('F');
else:
    print("Invalid marks")



