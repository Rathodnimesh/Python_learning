def oddeven(n):
    if n%2==0:
        print(n, "IS odd")
    else:
        print(n, "IS even")

def maxoftwo(a,b):
    if(a>b):
        print(a,"IS  max")
    else:
        print(b,"Is max")

def maxofthree(a,b,c):
    if(a>b):
        if a>c:
            print(a,"IS max")
        else:
            print(c,"IS max")
    elif b>c:
       print(b,"IS max")

    else:
        print(c,"IS max")

        
def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n,"IS not prime")
                break
            else:
                print(n,"IS prime")
    else:
        print(n,"IS not a prime")

def fibonacci(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()    






        






       
