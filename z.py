n = int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i == n-1 or i == 0:
            for k in range(n):
                str = str + "*"
            print(str)
        else :
            temp = n-1
            for k in range(n):
                if k == temp:
                    print("\r")
                else:
                    print("*")
                    temp -=1
            

