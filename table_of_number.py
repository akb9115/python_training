table_number = int(input("Enter the number to print its table:"))
x = 1
while x<=10:
    new_number = table_number * x
    print(table_number,"*",x,"=",new_number)
    x = x + 1