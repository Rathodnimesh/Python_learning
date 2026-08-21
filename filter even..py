l1=[23,34,45,67,23,98]



def checkeven(num):
    if num%2 == 0:
        return num


l2=list(filter(checkeven,l1))
print(l2)
