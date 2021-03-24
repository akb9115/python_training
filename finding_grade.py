marks = int(input("Enter the marks:"))
if marks<=100:
    if marks>80 and marks<=100:
        print("A Grade")
    elif marks>60 and marks<=80:
        print("B Grade")
    elif marks>40 and marks<=60:
        print("C Grade")
    else:
        print("Fail")
else:
    print("Invalid Input")