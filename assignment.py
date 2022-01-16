""" Write a program to check whether a number is prime, Armstrong or
perfect number using functions. """

def is_prime(n):
    """ Check if a number is prime """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    """ Check if a number is Armstrong """
    sum = 0
    for i in str(n):
        sum += int(i) ** len(str(n))
    return sum == n

def is_perfect(n):
    """ Check if a number is perfect """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def main():
    """ Main function """
    n = int(input("Enter a number: "))
    print("Prime: ", is_prime(n))
    print("Armstrong: ", is_armstrong(n))
    print("Perfect: ", is_perfect(n))


if __name__ == "__main__":
    main()
    
    
    
    
    #2
    
    
    import csv
reader = csv.reader(open("AirfoilSelfNoise.csv", "r"))
first = [float(i[1]) for i in reader]
reader2 = csv.reader(open("AirfoilSelfNoise.csv", "r"))
sixth = [float(j[5]) for j in reader2]
angle = float(input("Enter the angle of Attack:"))
sum = 0
count = 0
if angle not in set(first):
    print("The angle of attack is not in the data set")
    exit(0)
    
for i in range(len(first)):
     if angle == first[i]:
          sum += sixth[i]
          count += 1
print("The average of the values is:", sum/count)


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




""" Define a operator overloading member function which takes TWO
objects representing complex numbers and returns new complex number
which is the addition of two complex numbers. Define a suitable class
‘Complex’ to represent the complex number with appropriate member
functions and data members. Develop a program to read N (N >=2)
complex numbers and to compute the addition of N complex numbers
with operator overloading """

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f'{self.real} + {self.imag}i'

def main():
    c_list = []
    for i in range(int(input('Enter no of numbers: N>=2: '))):
        real = float(input(f'Enter real  of {i+1}: '))
        imag = float(input(f'Enter imaginary of {i+1}: '))
        c_list.append(Complex(real, imag))
    print(f'\nAddition of {len(c_list)} complex numbers:')
    for i in range(len(c_list)-1):

        print(f'{c_list[i]} + {c_list[i+1]} = {c_list[i] + c_list[i+1]}')

main()
