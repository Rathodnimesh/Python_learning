l1=[23,34,54,67,34]


def checkeven(num):
    if num%2 == 0:
        return "Even"
    else:
        return "odd"



l2=list(map(checkeven,l1))
print(l2)
