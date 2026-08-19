x=lambda a,b,c:a+b+c
print(x(5,7,9))


def oddeven(n):
    if n%2==0:
        print("Even:")
    else:
        print("odd:")

oddeven(9)


y=lambda a:"even" if a%2==0 else"odd"
print(y(6))


def maxoftwonumber(a,b):
    if(a>b):
        print(a,"IS max")
    else:
        print(b,"Is max")
    
maxoftwonumber(45,85)


n = lambda a, b: a if a > b else b
print(n(100,150))






    
