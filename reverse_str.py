# text = "hello world"[:: -1]
# print(text)

# def my_function(x):
#     return x[:: -1]
# my_text = my_function("i wonder how this text like backwards")
# # print(my_text)
# def new_function(x):
#     return x[:: -1]
# new_text = new_function("jai mata di")
# print(new_text)
#
# my_number = int(input("enter your private number:"))
# reversed_number = 0
# while my_number>0:
#     rem = my_number%10
#     reversed_number = reversed_number*10 + rem
#     my_number = my_number//10
# print(reversed_number)
#
# for i in range(1,6):
#     for j in range(0,i):
#         print("*", end="")
#     print()

# def my_function(x):
#     return x[:: -1]
# new_text = my_function("sri ram")
# print(new_text)

# my_value = 68646323
# rever = 0
# while my_value>0:
#     rem = my_value%10
#     rever = rever * 10 + rem
#     my_value = my_value//10
# print(rever)

# for i in range(1,10):
#     for i in range(0,i):
#         print("$",end="")
#     print()

# ask for enter the number from the use
number = int(input("enter the integer number :"))

#intiate value to null
revs_number = 0
# reverse the integer number using the while loop
while(number>10):
    #logic
    remainder = number % 10
    revs_number= (revs_number*10) +remainder
    number = number//10
    #display the result
print("the reverse number is: {}".format(revs_number))