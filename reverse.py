# my_name = input("enter any string")
# result = ''
# for i in range(len(my_name)-1,-1,-1):
#     result = result + my_name[i]
#     print(result)
# using loop
# initialiging empty string
# run a loop from 'len(inputstr)-1 to 0 one by one append characters from end to start
# in result
# inputstr = 'geekforgeek'
# result = ''
# for i in range(len(inputstr)-1):
#     result = result + inputstr[i]
#     print(result)
#
# second formula for print reverse string

# my_str = input("enter the string :")
# reversechars = reversed(my_str)
# print("".join(reversechars))
# third formmula for print string character

# my_str = input("enter our string character:")
# print(my_str[-1: :-1])
# my_string = input("Enter your string:")
# l = len(my_string)
# reverse_string = ""
# for i in range(0,l):
#     reverse_string = my_string[i] + reverse_string
# if my_string == reverse_string:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# my_str = input("enter the string:")
# for i in range(len(my_str)):
#     print(my_str[i])
# name = "sanjit kumar"
# for i in range(len(name)):
#     print(name[i])
# name = "amit"
# for i in name:
#     print(i)
number = input("enter the number :")
total = 0
for i in number:
    total += int[i]
    print(total)