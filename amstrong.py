#Python program to print numbers between  and n which are amstrong

for num in range(100,10000):
    sum = 0
    temp = num
    while temp > 0:
        sum += (temp % 10) ** 3
        temp //= 10
    if num == sum:
        print(num)
    