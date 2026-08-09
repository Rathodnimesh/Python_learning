s=input("Enter your string:")

al=0
nm=0
sp=0
up=0
lo=0
sc=0

for i in s:
    if i.isalpha():
        al=al+1

        if i.isupper():
            up=up+1
        else:
            lo=lo+1
            
    elif i.isnumeric():
         nm=nm+1
    elif i.isspace():
         sp=sp+1

    else:
         sc=sc+1

print("Total alphabetic",al)
print("Toal numaric",nm)
print("Total space",sp)
print("Tota upper",up)
print("Tota low",lo)
print("spical charctor",sc)

          
