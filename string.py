# first_name = "lakshman"
# last_name = "Ajeet yadav"
# full_name = first_name + " " +last_name
# print(first_name + str("Lakshman"))
# print(full_name )

# number_one = input("enter the number:")
# number_two = input("enter the second number:")
# total = number_one + number_two
# print(total)
# def reverse(string):
#     reversed_string = ""
#     for i in string:
#         reversed_string = i + reversed_string
# print("reversed  string  is :" , reversed_string)
#
# string = input("enter a string :")
# print("entered string :" , string)
# reverse(string)
# my_str = input("enter the string:")
# for i in range(len(my_str)):
# #      print(my_str[i])
# name = "sanjit kumar"
# for i in range(len(name)):
#     print(name[i])
    # name = "amit"
    #     for i in name:
    #         print(my_str[i])
# my_str = input("enter the string:")
# for i in range(len(my_str)):
#     print(my_str[i])
# name = "nirahua"
# for i in name:
#     print(name[i])
my_str = str(input("Enter the number of your choice:"))
my_reversed_number = 0
while my_str>0:
    rem = my_str%10
    my_reversed_number = my_reversed_number*10 + rem
    my_str = my_str//10
print(my_reversed_number)

# my_number = int(input("enter the established number :"))
# new_number = 0
# while my_number>0:
#     rem = my_number%10
#     new_number = new_number*10 + rem
#     my_number = my_number // 10
# print(new_number)
# my_exit = 64934
# new_exit = 0
# while my_exit>0:
#     rem = my_exit%10
#     new_exit = new_exit * 10 + rem
#     my_exit = my_exit//10
# print(new_exit)
# my_external = int(input("enter our enternal number :"))
# new_exte =0
# while my_external>0:
#     rem = my_external%10
#     new_exte = new_exte*10+rem
#     my_external = my_external//10
#     print(new_exte)