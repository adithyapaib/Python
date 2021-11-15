#Program to print factoraial of a number with recursion and find the binomial coefficient
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
fact = factorial(num)
print("The factorial of", num, "is", fact)
r = int(input("Enter a number: "))
c = int(input("Enter a number: "))
print("The binomial coefficient of", r, "and", c, "is", factorial(r) // (factorial(c) * factorial(r-c)))
