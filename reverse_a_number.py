my_num = int(input("Enter the number of your choice:"))
my_reversed_number = 0
while my_num>0:
    rem = my_num%10
    my_reversed_number = my_reversed_number*10 + rem
    my_num = my_num//10
print(my_reversed_number)


