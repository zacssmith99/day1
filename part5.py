marks = float(input("Enter marks: "))
if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=80:
    print("excellent")
elif marks>=60:
    print("egood")
elif marks>=40:
    print("pass")  
else:
    print("Fail") 