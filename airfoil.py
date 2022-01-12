import csv
from time import sleep
reader = csv.reader(open("AirfoilSelfNoise.csv", "r"))
first = [i[5] for i in reader]
b = [i[1] for i in reader]
print(first)


""" for row in reader:
    first.append(float(row[1]))
for r in reader:
    sixth.append(float(r[5]))
print(first)
 """


""" print("Enter the angle of inciddence:")
angle = float(input())
result = []
for i in range(2,len(first)):
    if angle == first[i]:
        result.append(sixth[i])
print(result) """
