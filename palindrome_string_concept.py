my_string = input("Enter your string:")
l = len(my_string)
reverse_string = ""
for i in range(0,l):
    reverse_string = my_string[i] + reverse_string
if my_string == reverse_string:
    print("Palindrome")
else:
    print("Not Palindrome")