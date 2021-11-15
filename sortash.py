l=[2,1,9,10,6,8]


def sort(l):
    for i in range(0,len(l)):
        print(l[i])
        if(l[i]>l[i+1]):
            t = l[i+1]
            l[i+1] = l[i]
            l[i]= t
            i=0
sort(l)
print(l)