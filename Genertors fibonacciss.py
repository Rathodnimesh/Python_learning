def fibonacci(nn):
    a,b=0,1
    for i in range(nn):
        yield a

        a,b=b,a+b

fib=fibonacci(15)
for num in fib:
    print(num,end= " ")
