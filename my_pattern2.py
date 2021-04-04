str1 = input()
l = str1.split()
length = int(l[0])
width = int(l[1])
middle = length // 2 + 1
limit = width // 2 - 1
flag = 1
check = 0
# ABOVE WELCOME
for i in range(limit, 0, -1):
    if (check != middle - 1):
        for j in range(0, limit):
            print("-", end='')
        for k in range(0, flag):
            print(".|.", end='')
        flag = flag + 2
        for l in range(0, limit):
            print("-", end='')
        print()
        limit = limit - 3
        check = check + 1
# WELCOME
width2 = 0
l = len("WELCOME")
width2 = width - l
mid_wel = width2 // 2
for i in range(0, mid_wel):
    print("-", end='')
print("WELCOME", end='')
for i in range(0, mid_wel):
    print("-", end='')
print()
k2 = length - 2
# BELOW WELCOME
for i in range(0, middle - 1):
    for j in range(0, i * 3 + 3):
        print("-", end='')
    for k in range(0, k2):
        print(".|.", end='')
    k2 = k2 - 2
    for l in range(0, i * 3 + 3):
        print("-", end='')
    print()



