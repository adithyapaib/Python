#write program to swap two numbers

def swap(a, b):
    return b, a
a , b =  int(input("Enter first number: ")), int(input("Enter second number: "))
print("Before swapping: ", a, b)
a, b = swap(a, b)
print("After swapping: ", a, b)
