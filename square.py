#function generate square and swquare root of a anuber. Write a program that reads a number from the user,
import math 
def square_root(number):
    return number**2 , math.sqrt(number)
num_strr = input("Enter a number: ")
num_int = int(num_strr)
sqr, root = square_root(num_int)
print("The square of {} is {} and the square root of {} is {}".format(num_int, sqr, num_int, root))