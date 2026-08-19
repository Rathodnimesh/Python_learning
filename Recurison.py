def factorial(n):
    #base case
    if n == 0 or n ==1:
        return 1
    #Recursive case
    else:
        return n* factorial(n-1)

#Testing the function
print(factorial (15))
