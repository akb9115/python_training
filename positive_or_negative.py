
marks = int(input("enter the number and getting the percentage:"))
if(marks <= 100):
    if(marks >80 and marks <= 100):
        print("you are topper:")
    elif(marks > 60 and marks <= 80):
        print("you are first devision")
    elif(marks > 45 and marks <= 60):
        print("you are second devision")
    elif(marks >= 33 and marks <= 45):
        print("you are third devision")
    else:
        print("you are fail")
else:
    print("Invalid number")



