''' Program to read cricketer's achivement during his carrer interms of year runs scored and wickets. Sort the achivement of a cricket in the order of urns scored and wickets'''

a = list()
temp = list([0,10,3])
n = int(input("Enter the number of cricketers "))
for i in range(n):
    print("Data entry")
    print("Enter the data of Cricketer " + n+1)
    temp[0] = int(input("Enter the year"))
    temp[1] = int(input("Enter runs scored"))
    temp[2] = int(input("Enter the number of wickets taken"))
    a.append(temp)

for i in range(n):
    if(a[i][1]> a[i+1][1] )
