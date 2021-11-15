
#write a function to swap 2 array elements write a program to read n elements and sort the elements using selection sort method


def swap(a,i,j):
    t = a[i]
    a[j] = a[i]
    a[j] = t
    return a

def selection(a):
    n = int(input("Enter the number of elements"))
    for i in range(n):
        temp = int(input("Enter the element"))
        a.append(temp)
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                a = swap(a,i,j)
    print(a)
selection([])

