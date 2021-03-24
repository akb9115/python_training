seconds = int(input("enter the number of seconds:"))
hour = seconds//3600
remaining_seconds = seconds%3600
minutes = remaining_seconds//60
final_remaining_seconds = remaining_seconds%60
print(hour,"hours",minutes,"minutes",final_remaining_seconds,"seconds")