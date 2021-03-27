my_name = input("enter any string")
result = ''
for i in range(len(my_name)-1,-1,-1):
    result = result + my_name[i]
#     print(result)
# using loop
# initialiging empty string
# run a loop from 'len(inputstr)-1 to 0 one by one append characters from end to start
# in result
inputstr = 'geekforgeek'
result = ''
for i in range(len(inputstr)-1):
    result = result + inputstr[i]
    print(result)
#
# second formula for print reverse string

my_str = input("enter the string :")
reversechars = reversed(my_str)
print("".join(reversechars))
# third formmula for print string character

my_str = input("enter our string character:")
print(my_str[-1: :-1])