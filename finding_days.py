number_of_days = int(input("enter the finding days"))
year = number_of_days//365
rm = number_of_days%365
month = rm//30
days = rm%30
print(year,"years",month,"months",days,"days")